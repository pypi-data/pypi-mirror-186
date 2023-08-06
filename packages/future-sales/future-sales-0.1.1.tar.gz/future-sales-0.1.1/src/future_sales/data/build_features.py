from typing import Union

import numpy as np
import numpy.typing as npt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA

from future_sales.data.utils import reduce_mem_usage


def extract_shop_features(df: pd.DataFrame, shops: pd.DataFrame) -> pd.DataFrame:
    shops["city"] = shops["shop_name"].apply(lambda shop_name: shop_name.split()[0])
    shops["city"] = shops["city"].replace("!", "", regex=True)
    shops["city_code"] = shops["city"].factorize()[0]

    shops["shop_type"] = shops["shop_name"].apply(
        lambda shop_name: shop_name.split()[1]
        if shop_name.split()[1] in ["ТЦ", "ТРК", "ТРЦ", "ТК"]
        else "-"
    )
    shops["shop_type_code"] = shops["shop_type"].factorize()[0]

    shops["shop_first_month"] = df.groupby("shop_id")["date_block_num"].min()
    shops["shop_last_month"] = df.groupby("shop_id")["date_block_num"].max()

    shops.dropna(axis=0, inplace=True)

    return shops[
        [
            "shop_id",
            "city_code",
            "shop_type_code",
            "shop_first_month",
            "shop_last_month",
        ]
    ]


def extract_item_category_features(item_cats: pd.DataFrame) -> pd.DataFrame:
    item_cats["category_group"] = item_cats["item_category_name"].apply(
        lambda x: x.strip().split("-")[0]
    )
    item_cats["category_subgroup"] = item_cats["item_category_name"].apply(
        lambda x: x.strip().split("-")[1] if len(x.split("-")) > 1 else x.split("-")[0]
    )

    item_cats.loc[
        item_cats["category_group"].str.startswith("Игры"), "category_group"
    ] = "Игры"
    item_cats.loc[
        item_cats["category_group"] == "Карты оплаты (Кино, Музыка, Игры)",
        "category_group",
    ] = "Карты оплаты"
    item_cats.loc[
        item_cats["category_group"] == "Чистые носители (шпиль)", "category_group"
    ] = "Чистые носители"
    item_cats.loc[
        item_cats["category_group"] == "Чистые носители (штучные)", "category_group"
    ] = "Чистые носители"

    item_cats["category_group_code"] = item_cats["category_group"].factorize()[0]
    item_cats["category_subgroup_code"] = item_cats["category_subgroup"].factorize()[0]

    return item_cats[
        ["item_category_id", "category_group_code", "category_subgroup_code"]
    ]


def extract_item_features(df: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    items["item_first_sale"] = df.groupby("item_id")["date_block_num"].min()
    items["item_first_sale"] = items["item_first_sale"].fillna(34)
    return items[["item_id", "item_category_id", "item_first_sale"]]


def extract_cluster_feature(
    df: pd.DataFrame, cluster_name: str, n_clusters: int
) -> pd.DataFrame:
    # PCA:
    pca = PCA(n_components=2, random_state=42)
    components = pca.fit_transform(df)
    components = pd.DataFrame(components)

    # Clustering:
    clusterer = AgglomerativeClustering(n_clusters=n_clusters, linkage="average")
    labels = clusterer.fit_predict(components)

    df.insert(loc=0, column=cluster_name, value=labels)

    return df


def extract_lagged_features(
    df: pd.DataFrame, lags: list[int], col_name: str
) -> pd.DataFrame:
    for i in lags:
        feature_name = f"{col_name}_lag_{i}"
        shifted = df.copy()
        shifted.rename(columns={"item_cnt_month": feature_name}, inplace=True)
        shifted["date_block_num"] = shifted["date_block_num"] + i
        df = df.merge(
            shifted[["shop_id", "item_id", "date_block_num", feature_name]],
            on=["shop_id", "item_id", "date_block_num"],
            how="left",
        )
        df[feature_name] = df[feature_name].fillna(0)
    return df


def extract_rolling_window_features(
    df: pd.DataFrame, windows: list[int], col_name: str, agg_func: str
) -> pd.DataFrame:
    for w in windows:
        feature_name = f"{col_name}_rolling_{w}_{agg_func}"
        df[feature_name] = df.groupby(by=["shop_id", "item_id"], group_keys=False)[
            col_name
        ].apply(lambda x: x.rolling(window=3).agg(agg_func))
        df[feature_name] = df[feature_name].fillna(0)
    return df


def build_features(
    data: dict[str, pd.DataFrame],
    indices: Union[npt.NDArray[np.int_], list[int]],
    is_test: bool = False,
) -> pd.DataFrame:
    train = data["sales_train"].iloc[indices, :].copy()
    test = data["test"].set_index("ID").copy()
    shops = data["shops"].copy()
    items = data["items"].copy()
    item_cats = data["item_categories"].copy()

    # expand test set with same columns as train set so we can concatenate them row-wise
    if is_test:
        test["item_cnt_month"] = 0
        test["date_block_num"] = 34

        # merge train and test to build features
        dataset = pd.concat([train, test], axis=0)
    else:
        dataset = train.copy()

    # extract month and year
    dataset["year"] = dataset["date_block_num"].apply(lambda x: ((x // 12) + 2013))
    dataset["month"] = dataset["date_block_num"].apply(lambda x: (x % 12))

    # extract city name and shop type
    shops = extract_shop_features(df=dataset, shops=shops)

    shops = extract_cluster_feature(df=shops, cluster_name="shop_cluster", n_clusters=3)

    # extract category group/subgroup and fix some categories
    item_cats = extract_item_category_features(item_cats=item_cats)

    # extract first month sale, min item price, max item price
    items = extract_item_features(df=dataset, items=items)

    # items = extract_cluster_feature(
    #     df=items.merge(item_cats, on="item_category_id", how="left"),
    #     cluster_name="item_cluster",
    #     n_clusters=3,
    # )

    # extract lags of item_cnt_month
    dataset = extract_lagged_features(
        df=dataset, lags=[1, 2, 3, 4, 5, 6, 12], col_name="item_cnt_month"
    )

    # extract rolling window features
    dataset = extract_rolling_window_features(
        df=dataset, windows=[3], col_name="item_cnt_month", agg_func="mean"
    )

    # merge dataframes
    dataset = (
        dataset.merge(items, on="item_id", how="left")
        .merge(item_cats, on="item_category_id", how="left")
        .merge(shops, on="shop_id", how="left")
    )

    # drop unecessary column
    dataset.drop(columns=["item_price"], inplace=True)

    # cast dtypes
    dataset = reduce_mem_usage(dataset)

    if not is_test:
        return dataset
    else:
        return dataset[dataset["date_block_num"] == 34].drop(columns=["item_cnt_month"])

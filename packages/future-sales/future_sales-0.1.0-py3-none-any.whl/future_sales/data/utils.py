from itertools import product
import re
from typing import Callable

import numpy as np
import pandas as pd

MIN_PRICE: int = 0
MAX_PRICE: int = 300000
MIN_CNT: int = 0
MAX_CNT: int = 500


def cast_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    return df


def filter_neg_price(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["item_price"] > MIN_PRICE]


def filter_returns(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["item_cnt_day"] > MIN_CNT]


def filter_outliers_price(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["item_price"] < MAX_PRICE]


def filter_outliers_cnt(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["item_cnt_day"] < MAX_CNT]


def filter_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def clean_text(df: pd.DataFrame) -> pd.DataFrame:
    regex = re.compile("[^+a-zA-Zа-яА-Я0-9]+")
    col_name = [name for name in df.columns if "name" in name][0]
    df[col_name] = df[col_name].apply(lambda text: regex.sub(" ", text.strip().lower()))
    return df


def replace_duplicated_shop_ids(df: pd.DataFrame) -> pd.DataFrame:
    df["shop_id"] = df["shop_id"].replace({0: 57, 1: 58, 10: 11})
    return df


def expand_shop_item_grid(df: pd.DataFrame) -> pd.DataFrame:
    group_dfs = []
    for _, group_df in df.groupby("date_block_num"):
        group_dfs.append(
            pd.DataFrame(
                product(
                    group_df["shop_id"].unique(),
                    group_df["item_id"].unique(),
                    group_df["date_block_num"].unique(),
                ),
                columns=["shop_id", "item_id", "date_block_num"],
            )
        )

    expanded_df = pd.concat(group_dfs, axis=0).merge(
        group_df, how="left", on=["shop_id", "item_id", "date_block_num"]
    )

    return expanded_df


def group_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """Function that groups df by date_block_num,
    expands it with shop/item ids and sorts values by date_block_num"""
    # group by month
    monthly_sales = (
        df.groupby(["date_block_num", "shop_id", "item_id"])
        .agg({"item_price": "mean", "item_cnt_day": "sum"})
        .reset_index()
        .rename(columns={"item_cnt_day": "item_cnt_month"})
    )

    # expand (for every month create a grid from all shops/items combinations from that month)
    monthly_sales = expand_shop_item_grid(monthly_sales)

    monthly_sales["item_cnt_month"] = monthly_sales["item_cnt_month"].fillna(0)
    monthly_sales["item_price"] = monthly_sales["item_price"].fillna(0)
    monthly_sales["item_cnt_month"] = monthly_sales["item_cnt_month"].astype(int)
    # monthly_sales["item_cnt_month"] = monthly_sales["item_cnt_month"].clip(0, 20)

    # sort
    monthly_sales.sort_values(["date_block_num", "shop_id", "item_id"], inplace=True)

    return monthly_sales


def reduce_mem_usage(df: pd.DataFrame, silent: bool = True) -> pd.DataFrame:
    """
    Iterates through all the columns of a dataframe and downcasts the data type
     to reduce memory usage.
    """

    def downcast_numeric(series: pd.Series) -> pd.Series:
        """
        Downcast a numeric series into the smallest possible int/float dtype.
        """
        if pd.api.types.is_integer_dtype(series.dtype):
            series = pd.to_numeric(series, downcast="integer")
        if pd.api.types.is_float_dtype(series.dtype):
            series = pd.to_numeric(series, downcast="float")
        return series

    if not silent:
        start_mem = np.sum(df.memory_usage()) / 1024**2
        print("Memory usage of dataframe is {:.2f} MB".format(start_mem))

    for col in df.columns:
        df.loc[:, col] = downcast_numeric(df.loc[:, col])

    if not silent:
        end_mem = np.sum(df.memory_usage()) / 1024**2
        print("Memory usage after optimization is: {:.2f} MB".format(end_mem))
        print("Decreased by {:.1f}%".format(100 * (start_mem - end_mem) / start_mem))

    return df


transforms: dict[str, list[Callable[[pd.DataFrame], pd.DataFrame]]] = {
    "sales_train": [
        cast_to_datetime,
        filter_neg_price,
        filter_returns,
        filter_outliers_price,
        filter_outliers_cnt,
        filter_duplicates,
        replace_duplicated_shop_ids,
        group_by_month,
        reduce_mem_usage,
    ],
    "test": [
        replace_duplicated_shop_ids,
        reduce_mem_usage,
    ],
    "shops": [
        reduce_mem_usage,
    ],
    "items": [
        reduce_mem_usage,
    ],
    "item_categories": [
        reduce_mem_usage,
    ],
}

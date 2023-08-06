from functools import partial
from typing import Any, Generator, Union

from category_encoders import TargetEncoder
import click
from hyperopt import fmin, hp, tpe
import numpy as np
import numpy.typing as npt
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection._split import _BaseKFold
from sklearn.utils import indexable
from sklearn.utils.validation import _num_samples
from xgboost import XGBRegressor

from future_sales.data.build_features import build_features

RANDOM_STATE = 42
EARLY_STOPPING_ROUNDS = 10
SPACE = {
    "max_depth": hp.choice("max_depth", np.arange(3, 10, dtype=int)),
    "subsample": hp.uniform("subsample", 0.7, 1),
    "colsample_bytree": hp.uniform("colsample_bytree", 0.7, 1),
    "reg_lambda": hp.uniform("reg_lambda", 0, 1),
}
MAX_EVALS = 20


class GroupTimeSeriesSplit(_BaseKFold):  # type: ignore
    """
    Time Series cross-validator for a variable number of observations within the time unit.
    In the kth split, it returns first k folds as train set and the (k+1)th fold as test set.
    Parameters
    ----------
    n_splits : int, default=5
        Number of splits. Must be at least 2.
    """

    def __init__(self, *, n_splits: int = 5) -> None:
        super().__init__(n_splits, shuffle=False, random_state=None)

    def split(
        self,
        X: npt.NDArray[Union[np.int_, np.float_]],
        groups: npt.NDArray[np.int_],
    ) -> Generator[tuple[npt.NDArray[np.int_], npt.NDArray[np.int_]], None, None]:
        """Generate indices to split data into training and test set.
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.
        groups : array-like of shape (n_samples,)
            Group labels for the samples used while splitting the dataset into
            train/test set.
        Yields
        ------
        train : ndarray
            The training set indices for that split.
        test : ndarray
            The testing set indices for that split.
        """
        X, groups = indexable(X, groups)
        n_samples = _num_samples(X)
        indices = np.arange(n_samples)
        _, group_counts = np.unique(groups, return_counts=True)
        folds = np.split(indices, np.cumsum(group_counts)[:-1])
        n_folds = _num_samples(folds)
        test_starts = range(1, n_folds, 1)
        for test_start in test_starts:
            yield (
                np.concatenate(folds[:test_start]),
                np.concatenate(folds[test_start : test_start + 1]),
            )


def evaluate(
    data: dict[str, pd.DataFrame]
) -> tuple[float, TargetEncoder, pd.DataFrame]:
    X = data["sales_train"]

    gtscv = GroupTimeSeriesSplit(n_splits=33)
    groups = X["date_block_num"]
    folds = gtscv.split(X, groups=groups)

    cat_cols = [
        "shop_id",
        "item_id",
        "item_category_id",
        "item_first_sale",
        "city_code",
        "shop_type_code",
        "category_group_code",
        "category_subgroup_code",
        "shop_first_month",
        "shop_last_month",
        "year",
        "month",
        "shop_cluster",
        # "item_cluster",
    ]

    cv_scores = []
    preprocessed_dataset = []  # type: ignore
    for train_id, val_id in folds:
        click.echo(f"Current validation set: {np.unique(groups[val_id])}")

        # train set
        if len(preprocessed_dataset) == 0:
            X_train_full = build_features(data, indices=train_id)
        else:
            X_train_full = pd.concat((X_train_full, preprocessed_dataset.pop()))

        X_train, y_train = (
            X_train_full.drop(columns=["item_cnt_month"]),
            X_train_full["item_cnt_month"],
        )
        # y_train = y_train.clip(0, 20)
        click.echo(f"Train dataset shape: {X_train.shape}")

        # val set
        X_val_full = build_features(
            data, indices=np.concatenate((train_id, val_id))
        ).iloc[-len(val_id) :, :]
        preprocessed_dataset.append(X_val_full)
        X_val, y_val = (
            X_val_full.drop(columns=["item_cnt_month"]),
            X_val_full["item_cnt_month"],
        )
        # y_val = y_val.clip(0, 20)
        click.echo(f"Val dataset shape: {X_val.shape}\n")

        te = TargetEncoder(cols=cat_cols)
        te.fit(X_train, y_train)
        X_train = te.transform(X_train)
        X_val = te.transform(X_val)

        model = XGBRegressor(
            eval_metric="rmse",
            early_stopping_rounds=EARLY_STOPPING_ROUNDS,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        )
        model.fit(
            X_train,
            y_train,
            eval_set=[(X_train, y_train), (X_val, y_val)],
            verbose=False,
        )
        cv_scores.append(model.best_score)

    X_train_full = pd.concat((X_train_full, preprocessed_dataset.pop()))

    return np.array(cv_scores).mean(), te, X_train_full


def objective(space: dict[str, pd.DataFrame], data: pd.DataFrame) -> Any:
    X_train, X_val = (
        data[data["date_block_num"] <= 30],
        data[data["date_block_num"] > 30],
    )
    X_train, y_train = (
        X_train.drop(columns=["item_cnt_month"]),
        X_train["item_cnt_month"],
    )
    # y_train = y_train.clip(0, 20)
    X_val, y_val = (
        X_val.drop(columns=["item_cnt_month"]),
        X_val["item_cnt_month"],
    )
    # y_val = y_val.clip(0, 20)

    model = XGBRegressor(
        max_depth=int(space["max_depth"]),
        reg_lambda=space["reg_lambda"],
        subsample=space["subsample"],
        colsample_bytree=space["colsample_bytree"],
        eval_metric="rmse",
        early_stopping_rounds=EARLY_STOPPING_ROUNDS,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(
        X_train,
        y_train,
        eval_set=[(X_train, y_train), (X_val, y_val)],
        verbose=False,
    )

    pred = model.predict(X_val)

    rmse = mean_squared_error(y_val, pred, squared=False)
    print(f"RMSE: {rmse}")

    return rmse


def optimize(data: pd.DataFrame) -> Any:
    best = fmin(
        fn=partial(objective, data=data),
        space=SPACE,
        algo=tpe.suggest,
        max_evals=MAX_EVALS,
    )
    return best

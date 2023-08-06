import os
from pathlib import Path
import pickle
from warnings import simplefilter

import click
from xgboost import XGBRegressor

from future_sales.data.build_features import build_features
from future_sales.data.etl import ETL
from future_sales.utils import evaluate, optimize, RANDOM_STATE

simplefilter(action="ignore", category=FutureWarning)


@click.command()
@click.option(
    "--input-dir",
    default="data/raw",
    type=click.Path(exists=True, dir_okay=True),
    show_default=True,
    help="Path to directory with raw data.",
)
@click.option(
    "--interim-dir",
    default="data/intermediate",
    type=click.Path(exists=True, dir_okay=True),
    show_default=True,
    help="Path to directory to save intermediate data that has been transformed.",
)
@click.option(
    "--save-dir",
    default="data/processed",
    type=click.Path(exists=True, dir_okay=True),
    show_default=True,
    help="Path to directory to save final data sets for modeling.",
)
@click.option(
    "--checkpoint-path",
    default="models/model.pkl",
    type=click.Path(dir_okay=False, writable=True),
    show_default=True,
    help="Path to save trained model.",
)
def train(
    input_dir: Path,
    interim_dir: Path,
    save_dir: Path,
    checkpoint_path: Path,
) -> None:
    # extract data
    if len(os.listdir(interim_dir)) == 0:
        etl = ETL(input_dir=input_dir, save_dir=interim_dir)
        click.echo("Extracting data...")
        data = etl.extract()
        click.echo("Transforming data...")
        data = etl.transform(data)
        click.echo("Saving transformed data...\n")
        etl.load(data)
    else:
        click.echo("Extracting data...")
        etl = ETL(input_dir=interim_dir, save_dir=interim_dir)
        data = etl.extract()

    # evaluate
    click.echo("Evaluating...")
    rmse, target_encoder, X_train = evaluate(data)
    click.echo(f"Validation RMSE: {rmse}")

    X_train.to_csv(os.path.join(save_dir, "train.csv"), index=False)

    # X_train = pd.read_csv(os.path.join(save_dir, "train.csv"))
    # X_test = pd.read_csv(os.path.join(save_dir, "test.csv"))

    # tune hyperparameters
    click.echo("Hyperparameters tuning...")
    best_params = optimize(X_train)
    print(f"Best hyperparameters: {best_params}")

    # train
    click.echo("Training...")
    X_train, y_train = (
        X_train.drop(columns=["item_cnt_month"]),
        X_train["item_cnt_month"],
    )
    # y_train = y_train.clip(0, 20)
    click.echo(f"Train dataset shape: {X_train.shape}")

    X_test = build_features(data, indices=list(range(X_train.shape[0])), is_test=True)
    X_test = target_encoder.transform(X_test)
    X_test.to_csv(os.path.join(save_dir, "test.csv"), index=False)

    model = XGBRegressor(
        **best_params,
        eval_metric="rmse",
        early_stopping_rounds=None,
        random_state=RANDOM_STATE,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    pickle.dump(model, open(checkpoint_path, "wb"))
    click.echo(f"Model is saved to {checkpoint_path}")

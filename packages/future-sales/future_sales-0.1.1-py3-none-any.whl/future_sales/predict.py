from pathlib import Path
import pickle

import click
import pandas as pd


@click.command()
@click.option(
    "--input-dir",
    default="data/processed/test.csv",
    type=click.Path(exists=True, dir_okay=False),
    show_default=True,
    help="Path to directory with preprocessed test data.",
)
@click.option(
    "--checkpoint-path",
    default="models/model.pkl",
    type=click.Path(exists=True, dir_okay=False),
    show_default=True,
    help="Path to checkpoint.",
)
@click.option(
    "--submission-path",
    default="submissions/submission.csv",
    type=click.Path(dir_okay=False, writable=True),
    show_default=True,
    help="Path to save submission file.",
)
def predict(input_dir: Path, checkpoint_path: Path, submission_path: Path) -> None:
    X = pd.read_csv(input_dir)

    model = pickle.load(open(checkpoint_path, "rb"))

    preds = model.predict(X)

    df = pd.DataFrame(preds, columns=["item_cnt_month"])
    df["ID"] = df.index
    df = df.set_index("ID")
    df.to_csv(submission_path)

    click.echo(f"Submission file is saved to {submission_path}.")

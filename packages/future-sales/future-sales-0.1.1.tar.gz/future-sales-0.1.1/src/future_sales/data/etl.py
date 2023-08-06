import os
from pathlib import Path
from typing import Callable

import pandas as pd

from future_sales.data.utils import transforms


class ETL:
    def __init__(self, input_dir: Path, save_dir: Path) -> None:
        self.input_dir = input_dir
        self.save_dir = save_dir

    def extract(self) -> dict[str, pd.DataFrame]:
        data = {}
        for _, _, filenames in os.walk(self.input_dir):
            for filename in filenames:
                data[filename.split(".")[0]] = pd.read_csv(
                    os.path.join(self.input_dir, filename)
                )

        return data

    def transform(self, data: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
        def process_df(
            df: pd.DataFrame, handlers: list[Callable[[pd.DataFrame], pd.DataFrame]]
        ) -> pd.DataFrame:
            _df = df.copy()
            for handler in handlers:
                _df = handler(_df)

            return _df

        transformed_data = {
            tbl_name: process_df(
                df=data[tbl_name],
                handlers=transforms[tbl_name] if tbl_name in transforms.keys() else [],
            )
            for tbl_name in data.keys()
        }
        return transformed_data

    def load(self, data: dict[str, pd.DataFrame]) -> None:
        for filename in data.keys():
            data[filename].to_csv(
                os.path.join(self.save_dir, f"{filename}.csv"), index=False
            )

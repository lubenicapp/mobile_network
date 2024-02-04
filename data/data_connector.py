from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd

from app.utils.log import logit

DATA_SOURCE = "./data/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv"


class CSVError(Exception):
    ...


class CSVDataConnector:
    """
    This class gives access to data from the csv file
    """
    def __init__(self, *, data_source: Union[Path, None] = None) -> None:
        """
        Args:
              data_source: path to CSV file, or NONE for default
        """
        self.data_source = data_source or DATA_SOURCE
        self.dataframe = None

    @logit
    def closest_results(self, *, x: float, y: float) -> list:
        """
        Returns the closest row for each provider based on Euclidean distance of both x, y
        """
        data = self.data
        data["distance"] = np.sqrt((data["x"] - x) ** 2 + (data["y"] - y) ** 2)
        return data.loc[data.groupby("Operateur")["distance"].idxmin()].to_dict(orient="records")

    @property
    @logit
    def data(self) -> pd.DataFrame:
        return self.dataframe or self._prepare_data()

    def _prepare_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.data_source, sep=";")
            df["Operateur"] = df["Operateur"].astype(int)
            self.dataframe = df
            return self.dataframe
        except Exception as e:
            raise CSVError('Unable to load data')

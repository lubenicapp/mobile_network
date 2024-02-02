import numpy as np
import pandas as pd
from typing import Union

from app.utils.log import logit

DATA_SOURCE = "./data/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv"


class CSVDataConnector:
    def __init__(self, *, data_source: Union[pd.DataFrame, None] = None) -> None:
        if data_source is None:
            self.data = pd.read_csv(DATA_SOURCE, sep=";")
        else:
            self.data = data_source
        self.data["Operateur"] = self.data["Operateur"].astype(int)

    @logit
    def closest_results(self, *, x: float, y: float) -> list:
        self.data["distance"] = np.sqrt(
            (self.data["x"] - x) ** 2 + (self.data["y"] - y) ** 2
        )

        return self.data.loc[
            self.data.groupby("Operateur")["distance"].idxmin()
        ].to_dict(orient="records")

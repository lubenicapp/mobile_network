from io import StringIO

import pandas as pd

from data import CSVDataConnector

CSV_DATA = """
Operateur;x;y;2G;3G;4G
20801;102980;6847973;1;1;0
20810;103113;6848661;1;1;0
20820;103114;6848664;1;1;1
20815;112032;6840427;0;1;1
20820;124571;6834344;1;1;1
"""


class TestCSVDataConnector:

    def test_closest_results_returns_one_entry_per_provider(self, tmp_path):
        """
        Checks that one row per provider is in the results
        """

        temp_csv = tmp_path / "temp.csv"
        with open(temp_csv, 'w') as f:
            f.write(CSV_DATA)

        cdc = CSVDataConnector(data_source=temp_csv)

        results = cdc.closest_results(x=1, y=2)
        results_operators = [item["Operateur"] for item in results]

        assert set(results_operators) == {20801, 20810, 20815, 20820}

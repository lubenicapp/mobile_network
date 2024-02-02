import warnings

import pyproj
import requests

from app.utils.log import logit

warnings.filterwarnings(action="ignore", category=FutureWarning)


class GovernmentLocator:

    ENDPOINT = "https://api-adresse.data.gouv.fr/search"

    @staticmethod
    @logit
    def locate_address(*, address: str) -> tuple:
        response = requests.get(GovernmentLocator.ENDPOINT, params={"q": address})
        first_result = response.json().get("features")[0]["geometry"]["coordinates"]
        return gps_to_lambert(first_result[0], first_result[1])


def gps_to_lambert(x, y):
    lambert = pyproj.Proj(
        "+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs"
    )
    wgs84 = pyproj.Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
    long, lat = pyproj.transform(wgs84, lambert, x, y)
    return long, lat

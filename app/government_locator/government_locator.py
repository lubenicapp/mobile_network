import requests
import warnings

from app.utils.log import logit

warnings.filterwarnings(action="ignore", category=FutureWarning)


class LocatorError(Exception):
    ...


class GovernmentLocator:
    """
    Wrapper around the API api-adresse.data.gouv.fr
    """
    ENDPOINT = "https://api-adresse.data.gouv.fr/search"

    @staticmethod
    @logit
    def locate_address(*, address: str) -> tuple:
        """
        Input:
            address: string address for a French location, example "16 rue poulet 75018 Paris"
        Output:
            x, y, location in lambert93 coordinates system for the first result suggested by th API

        (documentation : https://adresse.data.gouv.fr/api-doc/adresse)
        """
        response = requests.get(GovernmentLocator.ENDPOINT, params={"q": address})
        try:
            first_result = response.json().get("features")[0]["properties"]
            return first_result['x'], first_result['y']
        except IndexError:
            raise LocatorError(f"No results found for address {address}")

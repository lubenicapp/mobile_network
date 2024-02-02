from app.government_locator import GovernmentLocator
from app.utils.log import logit
from data import CSVDataConnector


class NetworkCoverage:

    RELEVANT_RESULT_MAX_DISTANCE = 5000  # m
    NETWORK_PROVIDERS = {
        20801: "orange",
        20810: "SFR",
        20815: "free",
        20820: "bouygues",
    }

    def __init__(self, *, address: str):
        self.address = address

    @property
    @logit
    def coverage(self):
        x, y = GovernmentLocator.locate_address(address=self.address)
        coverage_data = CSVDataConnector().closest_results(x=x, y=y)
        return self._format_results(coverage_data)

    def _format_results(self, coverage_data: list):
        results = {}
        for provider_data in coverage_data:
            data = provider_data
            if provider_data["distance"] > self.RELEVANT_RESULT_MAX_DISTANCE:
                data = {}
            results.update(
                {
                    self._provider_name(provider_data["Operateur"]): self._provider_network(data),
                }
            )
        return results

    @logit
    def _provider_name(self, code: int):
        return self.NETWORK_PROVIDERS.get(code, "Unknown provider")

    @staticmethod
    def _provider_network(provider_data):
        return {
            "2G": provider_data.get("2G") == 1,
            "3G": provider_data.get("3G") == 1,
            "4G": provider_data.get("4G") == 1,
        }

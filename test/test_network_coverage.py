from unittest.mock import patch

from app.network_coverage import NetworkCoverage


SAMPLE_DATA = [
    {
        "Operateur": 20801,
        "x": 651365.0,
        "y": 6863740.0,
        "2G": 1,
        "3G": 1,
        "4G": 1,
        "distance": 24.01454783194885,
    },
    {
        "Operateur": 20810,
        "x": 651378.0,
        "y": 6863677.0,
        "2G": 1,
        "3G": 1,
        "4G": 1,
        "distance": 40.424762420707275,
    },
    {
        "Operateur": 20815,
        "x": 651294.0,
        "y": 6863933.0,
        "2G": 0,
        "3G": 1,
        "4G": 0,
        "distance": 229.60340577728928,
    },
    {
        "Operateur": 20820,
        "x": 651362.0,
        "y": 6863742.0,
        "2G": 1,
        "3G": 0,
        "4G": 0,
        "distance": 26.867047503519917,
    },
]


class TestNetworkCoverage:
    @patch("app.network_coverage.GovernmentLocator")
    @patch("app.network_coverage.CSVDataConnector.closest_results")
    def test_coverage_contains_right_network_providers(
        self,
        mock_closest_results,
        mock_gov_locator,
    ):
        def locate_address(address):
            return 651365, 6863750

        mock_gov_locator.locate_address.side_effect = locate_address
        mock_closest_results.return_value = SAMPLE_DATA

        network = NetworkCoverage(address="carrefour des Poulets Cachan 94230")
        results = network.coverage

        assert 'orange' in list(results.keys())
        assert 'SFR' in list(results.keys())
        assert 'free' in list(results.keys())
        assert 'bouygues' in list(results.keys())

    @patch("app.network_coverage.GovernmentLocator")
    @patch("app.network_coverage.CSVDataConnector.closest_results")
    def test_coverage_contains_entry_for_each_network(
            self,
            mock_closest_results,
            mock_gov_locator,
    ):
        def locate_address(address):
            return 651365, 6863750

        mock_gov_locator.locate_address.side_effect = locate_address
        mock_closest_results.return_value = SAMPLE_DATA

        network = NetworkCoverage(address="rue poulet Paris 75000")
        results = network.coverage

        assert results['orange'].keys() == {'2G', '3G', '4G'}

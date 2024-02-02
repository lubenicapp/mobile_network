from fastapi import status
from requests import codes


class TestRootUrl:
    def test_get_with_no_params_returns_200(self, test_app):
        response = test_app.get('/')
        assert response.status_code == codes.ok

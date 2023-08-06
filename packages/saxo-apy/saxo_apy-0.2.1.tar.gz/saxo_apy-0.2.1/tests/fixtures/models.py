"""Models for test suite."""

import json

with open("tests/fixtures/dummy_app_config_sim.json", "r") as f:
    DUMMY_SIM_CONFIG = json.load(f)

with open("tests/fixtures/dummy_app_config_live.json", "r") as f:
    DUMMY_LIVE_CONFIG = json.load(f)

with open("tests/fixtures/dummy_access_token.txt", "r") as f:
    DUMMY_ACCESS_TOKEN = f.readline()


class MockAuthResponse:
    """Mock response to replace API requests with."""

    @staticmethod
    def json() -> dict:
        """Return JSON content of response."""
        return {
            "access_token": DUMMY_ACCESS_TOKEN,
            "token_type": "Bearer",
            "refresh_token_expires_in": 3600,
            "expires_in": 1200,
            "refresh_token": "11111111-1111-1111-1111-111111111111",
        }

    @property
    def status_code(self) -> int:
        """Mocked status code."""
        return 201

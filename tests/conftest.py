
import pytest
from script.deploy import deploy_favorites


@pytest.fixture
# scope="session" -> this will run the deployment only once
def favorites_contract(scope="session"):
    return deploy_favorites()
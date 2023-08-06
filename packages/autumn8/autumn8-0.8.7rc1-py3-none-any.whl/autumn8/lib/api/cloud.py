from typing import Any, Dict, Optional
import requests
from requests.auth import HTTPBasicAuth

from autumn8.cli.cli_environment import CliEnvironment
from autumn8.common.config.settings import ServiceProvider
from autumn8.lib.api.lab import require_ok_response, url_with_params
from autumn8.lib.api_creds import retrieve_api_creds


def get_running_deployments(
    organization_id: int,
    environment: CliEnvironment,
    model_id: Optional[int] = None,
    service_provider: Optional[ServiceProvider] = None,
):
    autodl_host = environment.value["host"]

    params: Dict[str, Any] = {"organization_id": organization_id}
    if model_id is not None:
        params["model_id"] = model_id
    if service_provider is not None:
        params["service_provider"] = service_provider

    deployments_api_route = f"{autodl_host}/api/cloud/deployments"
    # TODO: wrap the requests library in a custom class to handle common logic like auth and headers for json
    response = requests.get(
        url_with_params(deployments_api_route, params),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(*retrieve_api_creds()),
    )

    require_ok_response(response)
    return response.json()["deployments"]


def deploy(
    organization_id: int,
    environment: CliEnvironment,
    model_id: int,
    machine_type: str,
    service_provider: ServiceProvider,
):
    autodl_host = environment.value["host"]

    params = {
        "organization_id": organization_id,
        "model_id": model_id,
        "machine_type": machine_type,
        "cloud_service_provider": service_provider.value,
    }

    deployments_api_route = f"{autodl_host}/api/cloud/deployments"
    response = requests.post(
        url_with_params(deployments_api_route, params),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(*retrieve_api_creds()),
    )

    require_ok_response(response)
    return response.json()


def terminate_deployment(
    organization_id: int,
    environment: CliEnvironment,
    deployment_id: str,
    service_provider: ServiceProvider,
):
    autodl_host = environment.value["host"]

    params = {
        "organization_id": organization_id,
        "service_provider": service_provider.value,
    }

    deployments_api_route = (
        f"{autodl_host}/api/cloud/deployments/{deployment_id}"
    )
    response = requests.delete(
        url_with_params(deployments_api_route, params),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(*retrieve_api_creds()),
    )

    require_ok_response(response)
    return response.json()

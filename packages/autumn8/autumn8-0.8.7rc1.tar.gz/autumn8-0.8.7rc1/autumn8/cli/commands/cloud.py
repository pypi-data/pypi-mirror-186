import json

import click
from autumn8.common.config.settings import ServiceProvider
from autumn8.lib import logging
from autumn8.cli import options
from autumn8.lib.api import cloud

logger = logging.getLogger(__name__)


@options.use_environment
@options.use_organization_id
@options.use_cloud_provider(prompt=False)
@click.option(
    "-m",
    "--model_id",
    help="Model ID to get the deployments for",
    prompt_required=False,
    default=None,
)
def list_deployments(organization_id, model_id, environment, cloud_provider):
    """List running deployments."""
    logger.info("Fetching the list of deployments...")
    deployments = cloud.get_running_deployments(
        organization_id,
        environment,
        model_id=model_id,
        service_provider=cloud_provider,
    )

    click.echo(json.dumps(deployments, indent=4))
    return


@options.use_environment
@options.use_organization_id
@click.option(
    "-m",
    "--model_id",
    prompt=True,
    type=int,
    help="Model ID to deploy",
    # TODO: add a better interactive prompt listing all available models
)
@options.use_cloud_provider()
@click.option(
    "-hw",
    "-t",
    "--machine_type",
    prompt=True,
    type=str,
    help="Server type to use for the deployment",
    # TODO: add a better interactive prompt listing all available servers
)
def deploy(
    organization_id: int,
    model_id: int,
    machine_type: str,
    environment,
    cloud_provider: ServiceProvider,
):
    """Deploy a model from AutoDL onto cloud."""
    logger.info("Launching a new deployment...")
    deployments = cloud.deploy(
        organization_id,
        environment,
        machine_type=machine_type,
        service_provider=cloud_provider,
        model_id=model_id,
    )

    click.echo(json.dumps(deployments, indent=4))
    return


@options.use_environment
@options.use_organization_id
@options.use_cloud_provider()
@click.option(
    "-d",
    "--deployment_id",
    prompt=True,
    help="ID of the deployment to terminate",
)
def terminate_deployment(
    organization_id, deployment_id, environment, cloud_provider
):
    """Terminate a running deployment."""
    response = cloud.terminate_deployment(
        organization_id, environment, deployment_id, cloud_provider
    )
    click.echo(json.dumps(response, indent=4))

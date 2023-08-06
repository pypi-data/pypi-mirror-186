import questionary
from questionary import Choice

from autumn8.lib.api.lab import fetch_user_data


def get_user_organizations(user_data):
    return [mem["organization"] for mem in user_data["memberships"]]


def pick_organization_id(environment):
    user_data = fetch_user_data(environment)
    user_organizations = get_user_organizations(user_data)

    organization_id = questionary.select(
        "Choose organization",
        choices=[
            Choice(title=f"{org['name']} ({org['id']})", value=org["id"])
            for org in user_organizations
        ],
        use_shortcuts=True,
    ).unsafe_ask()
    return organization_id


def verify_organization_id_access(environment, organization_id):
    user_data = fetch_user_data(environment)
    user_organization_ids = [
        org["id"] for org in get_user_organizations(user_data)
    ]
    if organization_id not in user_organization_ids:
        raise Exception(
            f"The user {user_data['email']} does not belong to the organization of id={organization_id}"
        )

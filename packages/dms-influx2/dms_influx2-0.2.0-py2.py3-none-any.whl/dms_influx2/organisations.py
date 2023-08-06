from influxdb_client import OrganizationsApi, Organization

from dms_influx2.exceptions import OrganizationsApiError


class Organizations(OrganizationsApi):
    def __init__(self, client):
        super().__init__(client)

    def get_id_organization_by_name(self, org_name: str) -> str:
        org_id = list(filter(lambda x: x.name == org_name, self.find_organizations()))
        if not org_id:
            raise OrganizationsApiError(f"Organisation `{org_name}` does not exists")
        else:
            return org_id[0].id

    def get_organization(self, org_name: str) -> Organization:
        orgs = self.find_organizations(org=org_name)
        return orgs[0] if orgs else None

    def get_organization_by_name(self, org_name: str):
        org_id = list(filter(lambda x: x.name == org_name, self.find_organizations()))
        if not org_id:
            raise OrganizationsApiError(f"Organisation `{org_name}` does not exists")
        else:
            return org_id[0]


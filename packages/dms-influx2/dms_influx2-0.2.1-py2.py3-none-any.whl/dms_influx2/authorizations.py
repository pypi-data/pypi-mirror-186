from influxdb_client import AuthorizationsApi, Authorization

from dms_influx2.exceptions import BucketApiError


class Authorizations(AuthorizationsApi):
    def __init__(self, client):
        self.org = client.org
        self.organizations_api = client.organizations_api
        self.buckets_api = client.buckets_api
        super().__init__(client)

    def create_bucket_authorization(self, bucket_name, org_name=None, read_only=True, description=None):
        if org_name is None:
            org_name = self.org
        org = self.organizations_api().get_organization(org_name=org_name)
        bucket = self.buckets_api().find_bucket_by_name(bucket_name=bucket_name)

        permissions_read = {
            'action': 'read',
            'resource': {
                'id': bucket.id,
                'name': bucket.name,
                'org': org.name,
                'org_id': org.id,
                'type': 'buckets'
            }
        }
        permissions_write = {
            'action': 'write',
            'resource': {
                'id': bucket.id,
                'name': bucket.name,
                'org': org.name,
                'org_id': org.id,
                'type': 'buckets'
            }
        }
        permissions = [permissions_read]
        if not read_only:
            permissions.append(permissions_write)
        authorization = Authorization(org_id=org.id, permissions=permissions, description=description)
        return self.create_authorization(authorization=authorization)

    def create_single_bucket_authorization(self, bucket_name: str, description: str = None, org_name: str = None,
                                           write: bool = False, ) -> Authorization:
        if org_name is None:
            org_name = self.org

        if not self.buckets_api().bucket_exists(bucket_name=bucket_name):
            raise BucketApiError(f"Bucket '{bucket_name}' does not exists")

        return self.create_bucket_authorization(bucket_name=bucket_name,
                                                org_name=org_name,
                                                read_only=not write,
                                                description=description)

    def find_authorizations_by_description(self, description=None):
        auths = self.find_authorizations()
        auths_out = []
        for auth in auths:
            if auth.description == description:
                auths_out.append(auth)
        return auths_out

    def delete_all_bucket_authorizations(self):
        # Delete all authorizations

        for auth in self.find_authorizations():
            for perm in auth.permissions:
                if perm.resource.type != 'buckets':
                    break
            else:
                self.delete_authorization(auth)

    def get_or_create_bucket_authorization(self, bucket_name, read_only=True, active=True):
        # try authorization by name first
        # then name_readonly

        auth_description = f'{bucket_name}_readonly' if read_only else bucket_name

        # TODO
        # Try find authorization by description
        auth = self.find_authorizations_by_description(auth_description)
        if auth:
            auth = auth[0]
            for perm in auth.permissions:
                if perm.resource.type == 'buckets' and perm.resource.name == bucket_name:
                    return auth
        return self.create_bucket_authorization(bucket_name,
                                                org_name=None,
                                                read_only=read_only,
                                                description=auth_description)

    def __attach_bucket_auths_dict(self, auth):
        buckets_perm = {}
        for perm in auth.permissions:
            if perm.resource.type == 'buckets':
                if perm.resource.name not in buckets_perm:
                    buckets_perm[perm.resource.name] = []
                buckets_perm[perm.resource.name].append(perm.action)
        _auth = auth.to_dict()
        _auth['buckets'] = []
        for name, actions in buckets_perm.items():
            _auth['buckets'].append({
                'bucket_name': name,
                'read_only': 'write' not in actions
            })
        return _auth

    def get_bucket_authorization_dict(self, auth_id):
        auth = self.find_authorization_by_id(auth_id)
        return self.__attach_bucket_auths_dict(auth)

    def get_bucket_authorizations_dict(self, org_name=None, order_by_created=True):
        if org_name is None:
            org_name = self.org
        auths = self.find_authorizations_by_org_name(org_name=org_name)
        auths_out = []
        for auth in auths:
            _auth = self.__attach_bucket_auths_dict(auth)
            auths_out.append(_auth)
        if order_by_created:
            auths_out = sorted(auths_out, key=lambda b: b['created_at'], reverse=True)
        return auths_out








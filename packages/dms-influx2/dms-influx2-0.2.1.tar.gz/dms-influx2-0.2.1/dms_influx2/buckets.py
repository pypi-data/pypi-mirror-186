from influxdb_client import BucketsApi, Bucket, Authorization

from dms_influx2.exceptions import BucketApiError


class Buckets(BucketsApi):
    def __init__(self, client):
        self.org = client.org
        self.authorizations_api = client.authorizations_api
        self.organizations_api = client.organizations_api
        super().__init__(client)

    def _create_bucket(self, bucket_name: str, description: str = None, org_name: str = None) -> Bucket:
        if org_name is None:
            org_name = self.org
        org = self.organizations_api().get_organization(org_name=org_name)
        return self.create_bucket(bucket_name=bucket_name, org=org, description=description)

    def bucket_exists(self, bucket_name):
        return bool(self.find_bucket_by_name(bucket_name))

    def create_bucket_with_auth(self, bucket_name: str, description: str = None,
                                org_name: str = None) -> Authorization:
        """
        Create new bucket with authorization
        :param bucket_name: bucket name
        :param description: bucket description
        :param org_name: organization name
        :return: token
        """

        if org_name is None:
            org_name = self.org

        org = self.organizations_api().get_organization(org_name=org_name)
        bucket = self._create_bucket(bucket_name=bucket_name, description=description, org_name=org_name)
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
        permissions = [permissions_read, permissions_write]
        authorization = Authorization(org_id=org.id, permissions=permissions, description=description)
        return self.authorizations_api().create_authorization(authorization=authorization)

    def delete_permissions(self, bucket_name, org=None, read=True, write=True, delete_if_none=True):
        if org is None:
            org = self.org

        organization = self.organizations_api().get_organization_by_name(org_name=org)
        auths = self.authorizations_api().find_authorizations_by_org(organization)
        for auth in auths:
            orig_perm = list(auth.permissions)
            for perm in auth.permissions:
                if locals()[perm.action]:
                    if perm.resource.name == bucket_name:
                        perm.resource.name = None
                        # auth.permissions[perm]
                        # auth.permissions.remove(perm)
            if orig_perm != auth.permissions:
                self.authorizations_api().update_authorization(auth=auth)
            if delete_if_none:
                if all([bool(i.resource.name is None and i.resource.id is not None) for i in auth.permissions]):
                    self.authorizations_api().delete_authorization(auth=auth)

    def delete_bucket_by_name(self, bucket_name: str):
        bucket = self.find_bucket_by_name(bucket_name=bucket_name)
        if bucket is None:
            raise BucketApiError(f"Bucket {bucket_name} does not exists.")
        self.delete_bucket(bucket=bucket)

    def delete_bucket_by_id(self, bucket_id):
        bucket = self.find_bucket_by_id(bucket_id)
        if bucket is None:
            raise BucketApiError(f"Bucket {bucket_id} does not exists.")
        self.delete_bucket(bucket=bucket)

    def list_buckets(self, only_names=False):
        buckets = []
        offset = 0
        while True:
            _buckets = self.find_buckets(offset=offset, limit=100).buckets
            if not _buckets:
                break
            buckets += _buckets
            offset += 100
        if only_names:
            return [bucket.name for bucket in buckets]
        else:
            return buckets

    def get_buckets_dict(self, order_by_created=True):
        buckets = [bucket.to_dict() for bucket in self.list_buckets()]
        if order_by_created:
            buckets = sorted(buckets, key=lambda b: b['created_at'], reverse=True)
        # buckets_out
        # for bucket in buckets:
        #     created_at = bucket['created_at']
        #     bucket['created_at'] = bucket['created_at'].tzinfo
        #     datetime(2021, 12, 6, 13, 33, 10, 146344).strftime("%Y-%m-%d %H:%M:%S")
        return buckets

    def bucket_exists_by_id(self, bucket_id):
        return bool(self.find_bucket_by_id(id=bucket_id))

    def change_bucket_description(self, bucket_id, description):
        bucket = self.find_bucket_by_id(bucket_id)
        bucket.description = description
        return self.update_bucket(bucket)


    def create_bucket_with_default_authorizations(self, bucket_name, bucket_description=None):
        """
        Create bucket with two authorizations:
        - read/write auth with description == bucket_name
        - read auth with description == bucket_name_readonyl

        """
        if bucket_description is None:
            bucket_description = bucket_name
        bucket = self._create_bucket(bucket_name=bucket_name, description=bucket_description)

        # read/write
        self.authorizations_api().create_bucket_authorization(bucket_name=bucket_name,
                                                              read_only=False,
                                                              description=bucket_name)

        # read
        self.authorizations_api().create_bucket_authorization(bucket_name=bucket_name,
                                                              read_only=True,
                                                              description=bucket_name + '_readonly')

        return bucket


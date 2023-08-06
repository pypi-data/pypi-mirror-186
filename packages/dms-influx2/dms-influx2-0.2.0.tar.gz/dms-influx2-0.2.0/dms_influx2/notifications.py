from influxdb_client import NotificationEndpointsService, HTTPNotificationEndpoint, NotificationRulesService, \
    HTTPNotificationRule, StatusRule, RuleStatusLevel, TaskStatusType
from influxdb_client.rest import ApiException

from dms_influx2.exceptions import NotificationError


class NotificationEndpointApi(NotificationEndpointsService):
    def __init__(self, client):
        self.org = client.org
        self.org_id = client.organizations_api().get_id_organization_by_name(self.org)
        super().__init__(api_client=client.api_client)

    def get_all_notification_endpoints(self):
        return self.get_notification_endpoints(org_id=self.org_id)

    def notification_endpoints_id_exists(self, endpoint_id):
        try:
            self.get_notification_endpoints_id(endpoint_id)
            return True
        except ApiException as e:
            if e.status == 404 or e.status == 400:
                return False

    def add_http_notification(self, name, url, description=None):
        endpoint = HTTPNotificationEndpoint(name=name,
                                            url=url,
                                            org_id=self.org_id,
                                            method='POST',
                                            auth_method="none",
                                            description=description)
        service = NotificationEndpointsService(api_client=self.api_client)
        try:
            return service.create_notification_endpoint(endpoint)
        except ApiException as e:
            if e.status == 422:
                raise NotificationError(f"Notification endpoint with name '{name}' already exists.")


class NotificationRuleApi(NotificationRulesService):
    def __init__(self, client):
        self.org = client.org
        self.org_id = client.organizations_api().get_id_organization_by_name(self.org)
        super().__init__(api_client=client.api_client)

    def get_all_notification_rules(self):
        return self.get_notification_rules(org_id=self.org_id)

    def notification_rule_id_exists(self, rule_id):
        try:
            self.get_notification_rules_id(rule_id)
            return True
        except ApiException as e:
            if e.status == 404 or e.status == 400:
                return False

    def add_notification_rule(self, name, endpoint_id, status_rules=None):
        if status_rules is None:
            status_rules = [
                {
                    'count': None,
                    'current_level': 'ANY',
                    'period': None,
                    'previous_level': 'ANY'
                }
            ]
        notification_rule = HTTPNotificationRule(name=name,
                                                 every="5s",
                                                 offset="0s",
                                                 status_rules=[StatusRule(previous_level=RuleStatusLevel.ANY,
                                                                          current_level=RuleStatusLevel.ANY)],
                                                 tag_rules=[],
                                                 endpoint_id=endpoint_id,
                                                 org_id=self.org_id,
                                                 status=TaskStatusType.ACTIVE)

        service = NotificationRulesService(api_client=self.api_client)
        return service.create_notification_rule(notification_rule)

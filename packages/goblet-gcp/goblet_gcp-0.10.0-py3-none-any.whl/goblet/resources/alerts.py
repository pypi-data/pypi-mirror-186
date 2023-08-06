import logging

from goblet.resources.handler import Handler
from goblet.client import (
    get_default_project,
    get_default_location,
)
from goblet.common_cloud_actions import get_cloudrun_url
from goblet.config import GConfig

from googleapiclient.errors import HttpError

log = logging.getLogger("goblet.deployer")
log.setLevel(logging.INFO)


class Alerts(Handler):
    """Cloud Monitoring Alert Policies that can trigger notification channels based on built in or custom metrics.
    https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies
    """

    resource_type = "alerts"
    valid_backends = ["cloudfunction", "cloudfunctionv2", "cloudrun"]
    can_sync = True

    def register_alert(self, name, condition, notification_channels):
        # custom log condition?
        self.resources[name] = {
            "name":name,
            "condition": condition,
            "notification_channels": notification_channels
        }

    def _deploy(self, source=None, entrypoint=None, config={}):
        if not self.resources:
            return

        log.info("deploying alerts......")
        for alert_name, alert in self.resources.items():
            pass
            # self.deploy_job(job_name, job["job_json"])

    def _sync(self, dryrun=False):
        jobs = self.versioned_clients.cloudscheduler.execute("list").get("jobs", [])
        filtered_jobs = list(
            filter(lambda job: f"jobs/{self.name}-" in job["name"], jobs)
        )
        for filtered_job in filtered_jobs:
            split_name = filtered_job["name"].split("/")[-1].split("-")
            filtered_name = split_name[1]
            if not self.resources.get(filtered_name):
                log.info(f'Detected unused job in GCP {filtered_job["name"]}')
                if not dryrun:
                    # TODO: Handle deleting multiple jobs with same name
                    self._destroy_job(filtered_name)

    def deploy_job(self, job_name, job):
        try:
            self.versioned_clients.cloudscheduler.execute(
                "create", params={"body": job}
            )
            log.info(f"created scheduled job: {job_name} for {self.name}")
        except HttpError as e:
            if e.resp.status == 409:
                log.info(f"updated scheduled job: {job_name} for {self.name}")
                self.versioned_clients.cloudscheduler.execute(
                    "patch",
                    parent_key="name",
                    parent_schema=job["name"],
                    params={"body": job},
                )
            else:
                raise e

    def destroy(self):
        if not self.resources:
            return
        for job_name in self.resources.keys():
            self._destroy_job(job_name)

    def _destroy_job(self, job_name):
        try:
            self.versioned_clients.cloudscheduler.execute(
                "delete",
                parent_key="name",
                parent_schema="projects/{project_id}/locations/{location_id}/jobs/"
                + self.name
                + "-"
                + job_name,
            )
            log.info(f"Destroying scheduled job {job_name}......")
        except HttpError as e:
            if e.resp.status == 404:
                log.info("Scheduled jobs already destroyed")
            else:
                raise e

class AlertCondition:
    def __init__(self, name, threshold=None, absence=None, log_match=None, MQL=None) -> None:
        self.name = name
        if [threshold, absence, log_match, MQL].count(None) != 1:
            raise ValueError("Exactly 1 condition option can be set")
        if threshold:
            self.condition_key = "conditionThreshold"
            self.condition = threshold
        if absence:
            self.condition_key = "conditionAbsent"
            self.condition = absence
        if log_match:
            self.condition_key = "conditionMatchedLog"
            self.condition = log_match
        if MQL:
            self.condition_key = "conditionMonitoringQueryLanguage"
            self.condition = MQL

    @property
    def condition(self):
        return {
            "displayName": self.name,
            self.condition_key:self.condition
        }

class MetricCondition(AlertCondition):
    # https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold
    def __init__(self, name, value,duration="60s", **kwargs) -> None:
        # "filter": "resource.type = \"pubsub_subscription\" AND metric.type = \"pubsub.googleapis.com/subscription/oldest_unacked_message_age\"",

        super().__init__(name=name,threshold={
            "filter":,
            "thresholdValue": value,
            "duration":duration,
            **kwargs
        } )

class ErrorCondition(AlertCondition):
    def __init__(self) -> None:
        super().__init__()

#           "conditions": [
#     {
#       "displayName": "50X in media-serving-service",
#       "conditionThreshold": {
#         "filter": "metric.type=\"logging.googleapis.com/user/media-metadata-service-errors-metric\"",
#         "aggregations": [
#           {
#             "alignmentPeriod": "300s",
#             "crossSeriesReducer": "REDUCE_SUM",
#             "perSeriesAligner": "ALIGN_SUM"
#           }
#         ],
#         "comparison": "COMPARISON_GT",
#         "duration": "0s",
#         "trigger": {
#           "count": 1
#         },
#         "thresholdValue": 10
#       }
#     }
#   ],
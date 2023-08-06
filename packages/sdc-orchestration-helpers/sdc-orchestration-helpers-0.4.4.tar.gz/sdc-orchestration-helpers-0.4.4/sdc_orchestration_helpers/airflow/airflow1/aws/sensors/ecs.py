# pylint: disable=super-with-arguments
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

import logging

import boto3
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

logger = logging.getLogger(None)


class MonitorEcsTask(BaseSensorOperator):
    """
    Retrieves the metadata for a given job run and checks the run status.
    """

    template_fields = ("config", "xcom_tasks")

    @apply_defaults
    def __init__(self, config, xcom_tasks=None, *args, **kwargs):
        super(MonitorEcsTask, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def poke(self, context):
        """Monitors ECS Task Run Status"""

        CLIENT = boto3.client("ecs")

        task_cluster = self.config["task_cluster"]
        task_ids = self.xcom_tasks["task_run_id"]["task_id"]
        task_run_id = context["task_instance"].xcom_pull(
            task_ids=task_ids, key=self.xcom_tasks["task_run_id"]["key"]
        )

        try:
            response = CLIENT.describe_tasks(cluster=task_cluster, tasks=[task_run_id])
            ecs_task_definition_status = (
                response.get("tasks")[0].get("containers")[0].get("lastStatus")
            )
            logging.info(
                "Looking for ECS Task ID: {id} in Cluster: {cluster}".format(
                    id=task_run_id, cluster=task_cluster
                )
            )

            if ecs_task_definition_status in [
                "DEACTIVATING",
                "STOPPING",
                "DEPROVISIONING",
                "STOPPED",
            ]:
                return True
            elif ecs_task_definition_status in [
                "PROVISIONING",
                "PENDING",
                "ACTIVATING",
                "RUNNING",
            ]:
                return False
            else:
                raise Exception(
                    "training job status == {TASK_STATE} with reason = {REASON}".format(
                        TASK_STATE=ecs_task_definition_status, REASON=response
                    )
                )

        except Exception as err:
            raise err

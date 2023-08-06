# pylint: disable=super-with-arguments
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

import logging
import re

import boto3
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

logger = logging.getLogger(None)


class MonitorEcsTask(BaseSensorOperator):
    """
    Retrieves the metadata for a given job run and checks the run status.
    """

    template_fields = (
        "poke_interval",
        "timeout",
        "soft_fail",
        "mode",
        "xcom_tasks",
        "config",
    )

    @apply_defaults
    def __init__(
        self,
        poke_interval=60,
        timeout=60 * 60 * 24 * 7,
        soft_fail=False,
        mode="poke",
        xcom_tasks=None,
        config=None,
        *args,
        **kwargs,
    ):
        super(MonitorEcsTask, self).__init__(
            poke_interval=poke_interval,
            timeout=timeout,
            soft_fail=soft_fail,
            mode=mode,
            *args,
            **kwargs,
        )

        self.config = config
        self.xcom_tasks = xcom_tasks

    def poke(self, context):
        CLIENT = boto3.client("ecs")

        task_cluster = self.config["task_cluster"]
        task_ids = self.xcom_tasks["task_run_id"]["task_id"]
        task_run_id = context["task_instance"].xcom_pull(
            task_ids=task_ids, key=self.xcom_tasks["task_run_id"]["key"]
        )
        response = CLIENT.describe_tasks(cluster=task_cluster, tasks=[task_run_id])
        logging.info(f"Looking for ECS Task: {task_run_id} in Cluster: {task_cluster}")
        try:
            if len(response.get("failures", [])) > 0:
                raise Exception(response.get("failures"))

            task = response["tasks"][0]
            task_stop_reason = task.get("stoppedReason", "")
            if task.get("stopCode", "") == "TaskFailedToStart":
                raise Exception(f"The task failed to start due to: {task_stop_reason}")

            #     # This is a `stoppedReason` that indicates a task has not successfully
            #     # finished, but there is no other indication of failure in the response.
            #     # https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-errors.html
            if re.match(
                r"Host EC2 \(instance .+?\) (stopped|terminated)\.", task_stop_reason
            ):
                raise Exception(
                    f"The task was stopped because the host instance terminated: {task_stop_reason}"
                )
            containers = task["containers"]
            running_statuses = [
                "PROVISIONING",
                "PENDING",
                "ACTIVATING",
                "RUNNING",
                "DEACTIVATING",
                "STOPPING",
                "DEPROVISIONING",
            ]
            for container in containers:
                container_name = container.get("name")
                container_last_status = container.get("lastStatus")
                container_reason = container.get("reason", "").lower()
                logging.info(f"Last Status : {container_last_status}")
                if container_last_status == "STOPPED":
                    if container["exitCode"] != 0:
                        raise Exception(
                            f"Container did not exit successfully {container_name}"
                        )
                    logging.info(f"Container exited successfully : {container_name}")
                    return True
                elif container_last_status in running_statuses:
                    return False
                elif "error" in container_reason:
                    raise Exception(
                        f"Container encountered an error when launching :{container_name} : {container_reason}"
                    )

        except Exception as err:
            raise err

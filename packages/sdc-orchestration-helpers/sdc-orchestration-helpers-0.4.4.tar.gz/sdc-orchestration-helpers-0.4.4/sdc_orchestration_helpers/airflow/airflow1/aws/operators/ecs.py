# pylint: disable=super-with-arguments
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

"""
    ECS TASK CODE
        - these are used in pythonOperator steps as a way \
            to flexibly call boto3 and perform any special requirements
"""
import logging
import time

import boto3
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

logger = logging.getLogger(None)


class RunEcsTask(BaseOperator):
    """Run ECS Task Definition."""

    template_fields = (
        "config",
        "xcom_tasks",
    )

    @apply_defaults
    def __init__(self, config=None, xcom_tasks=None, *args, **kwargs):
        super(RunEcsTask, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """
        Triggers ECS Task Definition
        """
        CLIENT = boto3.client("ecs")

        task_definition_name = self.config.get("task_definition_name")
        task_cluster = self.config.get("task_cluster")
        security_groups = self.config.get("security_groups")
        subnets = self.config.get("subnets")

        try:
            log_message = """
                Running task: {name} with configurations:
                ecs_task_cluster: {cluster}
                security_groups: {security_groups}
                subnets: {subnets}
                """.format(
                name=task_definition_name,
                cluster=task_cluster,
                security_groups=security_groups,
                subnets=subnets,
            )
            logging.info(log_message)

            response = CLIENT.run_task(
                cluster=task_cluster,
                group=task_definition_name,
                launchType="FARGATE",
                networkConfiguration={
                    "awsvpcConfiguration": {
                        "subnets": subnets,
                        "securityGroups": security_groups,
                        "assignPublicIp": "ENABLED",
                    }
                },
                propagateTags="TASK_DEFINITION",
                taskDefinition=task_definition_name,
            )

            logging.info(response)

            ecs_task_run_id = response["tasks"][0]["containers"][0]["taskArn"].split(
                "/"
            )[-1]
            context["task_instance"].xcom_push(key="task_run_id", value=ecs_task_run_id)

        except Exception as err:
            raise err

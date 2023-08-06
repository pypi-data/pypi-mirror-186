# pylint: disable=super-with-arguments
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

"""
EventBus Send Event
To send event(s) into the bus, POST an array of events to the /events endpoint.
"""
import json
import logging
from datetime import datetime

import boto3
import requests
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

logger = logging.getLogger(None)

DAG_EVENTS = ["DagStarting", "DagRunning", "DagSucceeded", "DagFailed", "DagStopped"]


class SendDagStatus(BaseOperator):
    """
    https://docs.bus.ritdu.net/send-events.html#using-a-client-library
    To send event(s) into the bus, POST an array of events to the /events endpoint.

    :param config: consumes a configuration object:
        username: ''
        password: ''
        node_id: ''
        venture_token_bucket: ''
        venture_token_key: ''
        event: ''
        payload:
            "dag_name": "dl__google_analytics__horizon__downstream_data",
            "vendor": "google_analytics",
            "vertical": "horizon",
            "process": "downstream, staging, historical",
    """

    template_fields = ("config", "xcom_tasks")

    @apply_defaults
    def __init__(self, config, xcom_tasks=None, *args, **kwargs):
        super(SendDagStatus, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

        self.s3_resource = boto3.resource("s3")
        self.header = None

    def get_cached_venture_token(self):
        """
        Get the token object directly from the secure s3 bucket,
        and set it as the header of the request.
        """
        logging.info(
            f"Getting Venture Token at s3://{self.config['venture_token_bucket']}/{self.config['venture_token_key']}."
        )
        local_path = self.config["venture_token_key"].split("/")[-1]
        self.s3_resource.Object(
            self.config["venture_token_bucket"], self.config["venture_token_key"]
        ).download_file(local_path)

        with open(local_path, "r") as file:
            data = json.loads(file.read())

        return data.get("token")

    def update_cached_venture_token(self, token_object: dict):
        """
        Sends new token json object to secure s3 bucket.
        """
        logging.info("Updating Venture Token.")
        s3_object = self.s3_resource.Object(
            self.config["venture_token_bucket"], self.config["venture_token_key"]
        )
        s3_object.put(Body=json.dumps(token_object))

    def refresh_cached_venture_token(self):
        """
        If we receive a 401, we can make use if this functionality to refresh toe token
        and save it in our aws service.
        """
        logging.info("Refreshing Venture Token.")
        response = requests.post(
            url="https://bus.ritdu.net/v1/login",
            json={
                "username": self.config.get("username", None),
                "password": self.config.get("password", None),
                "node_id": self.config.get("node_id"),
            },
        ).json()
        return response

    def execute(self, context):
        """
        To send event(s) into the bus, POST an array of events to the /events endpoint.
        """
        # try to keep event names consistent
        event = self.config.get("event")
        if event not in DAG_EVENTS:
            raise ValueError(
                f"Dag event name: {event} not consistent with events: {DAG_EVENTS}."
            )

        # run request and refresh token on response
        while True:
            logging.info("Attempting to send event...")
            self.header = {
                "Accept": "application/json",
                "Content-type": "application/json",
                "x-api-key": self.get_cached_venture_token(),
            }
            payload = [
                {
                    "events": [event],
                    "from": self.config.get("node_id"),
                    "reference": str(datetime.now().strftime("%s")),
                    "created_at": f"{datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%S.%f')[:-3]}Z",
                    "payload": {
                        "dag": {
                            "dag_name": self.config["payload"].get("dag_name"),
                            "vendor": self.config["payload"].get("vendor"),
                            "vertical": self.config["payload"].get("vertical"),
                            "process": self.config["payload"].get("process"),
                        }
                    },
                    "version": "2.0.0",
                    "route": "",
                },
            ]

            logging.info(payload)

            response = requests.post(
                url="https://bus.ritdu.net/v1/events", headers=self.header, json=payload
            )

            logging.info(f"Send Response: {response.json()}.")

            if response.status_code in [401, 403]:
                self.refresh_cached_venture_token()

            else:
                # stop attempts
                break

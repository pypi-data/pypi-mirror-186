import functools
import json
from typing import Dict, List, Optional, Union

import boto3


class BotAWSSQSPlugin:
    def __init__(self, region_name: str = 'us-east-1', use_credentials_file: Optional[bool] = True,
                 access_key_id: Optional[str] = None, secret_access_key: Optional[str] = None,
                 queue_name: Optional[str] = None, queue_url: Optional[str] = None, **kwargs) -> None:
        """
        BotAWSSQSPlugin

        Args:
            region_name (str): Default region when creating new connections.
            use_credentials_file (bool, optional): If set to True will make
                authentication via AWS credentials file.
            access_key_id (str, optional): AWS access key ID.
            secret_access_key (str, optional): AWS secret access key.
        """
        self._queue_name = queue_name
        self._queue_url = queue_url

        if use_credentials_file:
            self._client = boto3.client(service_name='sqs', **kwargs)
        else:
            self._client = boto3.client(
                service_name='sqs',
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name,
                **kwargs
            )

    @property
    def queue_name(self):
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name: str):
        self._queue_name = queue_name

    @property
    def queue_url(self):
        return self._queue_url

    @queue_url.setter
    def queue_url(self, queue_url: str):
        self._queue_url = queue_url

    @property
    def sqs_client(self):
        """
        Returns the aws client instance.

        Returns:
            sqs_instance: The aws client instance.
        """
        return self._client

    def create_queue(self, queue_name, **kwargs) -> str:
        """
        Creates a new standard or FIFO queue.

        Args:
            queue_name (str): The name of the new queue.

        Returns:
            dict: Returns the QueueUrl attribute of the created queue.
        """
        return self._client.create_queue(QueueName=queue_name, **kwargs)

    def list_queues(self, **kwargs) -> List:
        """
        Returns a list of your queues in the current region.

        Returns:
            list: A list of queues.
        """
        return self._client.list_queues(**kwargs)["QueueUrls"]

    def delete_queue(self, queue_url: Optional[str] = None, **kwargs) -> None:
        """
        Deletes the queue specified by the QueueUrl , regardless of the queue's contents.

        Args:
            queue_url (str, optional): The URL of the Amazon SQS queue to delete.
        """
        queue_url = queue_url or self._queue_url
        if queue_url is None:
            raise ValueError("Queue url is required.")
        self._client.delete_queue(QueueUrl=queue_url, **kwargs)

    @functools.lru_cache(maxsize=None)
    def get_queue_url(self, queue_name: Optional[str] = None, **kwargs) -> str:
        """
        Returns the URL of an existing Amazon SQS queue.
        
        Args:
            queue_name (str, optional): The name of the queue whose URL must be fetched. Maximum 80 characters. Valid values: alphanumeric characters, hyphens (-), and underscores (_).
        
        Returns:
            str: The URL of the given queue.
        """  # noqa
        queue_name = queue_name or self._queue_name
        if queue_name is None:
            raise ValueError("Queue name is required.")

        return self._client.get_queue_url(QueueName=queue_name, **kwargs)["QueueUrl"]

    def send_message(self, message_body: Union[str, Dict], queue_url: Optional[str] = None, **kwargs) -> Dict:
        """
        Delivers a message to the specified queue.

        Args:
            queue_url (str, optional): The URL of the Amazon SQS queue to which a message is sent.
            message_body (str or dict): The message to send. The minimum size is one character. The maximum size is 256 KB.

        Returns:
            dict: The response from the boto3.send_sessage service method, as returned by SQS.
        """  # noqa
        queue_url = queue_url or self._queue_url
        if queue_url is None:
            raise ValueError("Queue url is required.")

        if isinstance(message_body, dict):
            message_body = json.dumps(message_body)

        return self._client.send_message(QueueUrl=queue_url, MessageBody=message_body, **kwargs)

    def receive_message(self, queue_url: Optional[str] = None, **kwargs) -> List:
        """
        Retrieves one or more messages (up to 10), from the specified queue.

        Args:
            queue_url (str, optional): The URL of the Amazon SQS queue from which messages are received.

        Returns:
            messages: A list of messages.
        """
        queue_url = queue_url or self._queue_url
        if queue_url is None:
            queue_url = self.get_queue_url(queue_name=self.queue_name)

        response = self._client.receive_message(QueueUrl=queue_url, **kwargs)
        if "Messages" in response:
            return response["Messages"]
        return []

    def delete_message(self, receipt_handle: str, queue_url: Optional[str] = None, **kwargs):
        """
        Deletes the specified message from the specified queue.

        Args:
            receipt_handle (str): The receipt handle associated with the message to delete.
            queue_url (str, optional): The URL of the Amazon SQS queue from which messages are deleted.
        """
        queue_url = queue_url or self._queue_url
        if queue_url is None:
            raise ValueError("Queue url is required.")

        self._client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle, **kwargs)

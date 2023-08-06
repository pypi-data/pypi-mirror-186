#!/usr/bin/env python3
from typing import Dict, Callable
import os
import time
import json
import logging
from bdating_common.collect_default import collect_info_for_apps
#from bdating_common.json_logger import setup_logger

app_info = collect_info_for_apps()
sns_client = app_info['session'].client(
  'sns', region_name=app_info.get('aws_region'))
sqs_client = app_info['session'].client(
  'sqs', region_name=app_info.get('aws_region'),
  endpoint_url=f"https://sqs.{app_info.get('aws_region')}.amazonaws.com")


def report_event(
    _type: str,
    action: str,
    body: Dict[str, object],
    success: bool = True,
    source_id: str = None,
    fail_on_error: bool = False
):
    """Report event
    """
    log = logging.getLogger(__name__)
    log.debug(
        f"Event ({_type}, {action}) to be reported to {app_info.get('event_bus_topic')} with body {body}")
    try:
        sns_client.publish(
            TopicArn=app_info.get('event_bus_topic'),
            Message=json.dumps({
                'time': int(time.time()) * 1000,
                'type': _type,
                'source_id': source_id,
                'action': action,
                'body': body,
                'result': {
                    'success': success,
                },
            }),
            MessageAttributes={
                'type': {
                    'DataType': 'String',
                    'StringValue': _type,
                },
                'action': {
                    'DataType': 'String',
                    'StringValue': action,
                },
            },
        )
    except Exception as e:
        log.warning(e)
        if fail_on_error:
            raise e
    log.info(
        f"Event ({_type}, {action}) reported to {app_info.get('event_bus_topic')} ")


def consume_event_loop(queue: str, process_method: Callable):
    """A skeleton for event consumer.

    Args:
        queue (_type_): the event queue, can be name or simply queue url
        process_method (_type_): _description_
    """
    log = logging.getLogger(__name__)
    if queue.startswith("https"):
        queue_url = queue
    else:
        response = sqs_client.list_queues(
            QueueNamePrefix=queue,
        )
        queue_url = response['QueueUrls'][0]
    error_count = 0
    while True:
        try:
            log.debug("Retrieving event...")
            response = sqs_client.receive_message(
                QueueUrl=queue_url,
                AttributeNames=[
                  'SentTimestamp'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                  'All'
                ],
                WaitTimeSeconds=20
            )
            log.debug(f"Received event count {len(response.get('Messages', []))}")
            if 'Messages' in response:
                for message in response['Messages']:
                    try:
                        process_method(json.loads(message['Body']))
                        response = sqs_client.delete_message(
                            QueueUrl=queue_url,
                            ReceiptHandle=message['ReceiptHandle']
                        )
                        error_count = 0
                    except Exception as e:
                        # pub back.
                        log.warning(f"Failed to process message {message}, reason {e}")
                        sqs_client.change_message_visibility(
                            QueueUrl=queue_url,
                            ReceiptHandle=message['ReceiptHandle'],
                            VisibilityTimeout=2
                        ) 
        except Exception as e:
            log.warning(e)
            error_count += 1
            if error_count > 10:
                time.sleep(4)


if __name__ == '__main__':
    for _ in range(10):
        report_event(
            'test', 'test_action',
            body={"demo": f"this is a demo"},
        )

import os
import json
import logging
import boto3
#from bdating_common.json_logger import setup_logger


def collect_info_for_apps(
    namespace: str = None,
    whoami: str = None,
    aws_profile: str = None,
    aws_region: str = None,
    event_bus_topic: str = None,
):
    log = logging.getLogger(__name__) 
    if namespace is None:
        log.debug('Finding whoami from environments NAMESPACE')
    namespace = os.environ.get('NAMESPACE', 'local')
    if whoami is None:
        whoami = os.environ.get('WHO_AM_I', 'unknown')
        if not whoami.startswith(namespace):
            whoami = f"{namespace}-{whoami}"
    if aws_region is None:
        log.debug(
            'Trying to find aws region information from environment AWS_REGION')
        aws_region = os.environ.get('AWS_REGION')
    if aws_region is None:
        log.debug('Using default aws region: sydney (ap-southeast-2)')
        aws_region = 'ap-southeast-2'
    if aws_profile is None:
        log.debug(
          'Trying to find aws aws profile information from environment AWS_PROFILE')
        aws_profile = os.environ.get('AWS_PROFILE')
    
    session = boto3.Session(profile_name=aws_profile, region_name=aws_region)
    if event_bus_topic is None:
        log.debug(
          'Trying to find event bus from environment BUSINESS_EVENT_BUS_TOPIC')
        event_bus_topic = os.environ.get('BUSINESS_EVENT_BUS_TOPIC')
        if not event_bus_topic:
            log.debug('Trying to construct event bus from account')
            sts_client = session.client('sts')
            client_info = sts_client.get_caller_identity()
            account = client_info.get('Account')
            event_bus_topic = f"arn:aws:sns:{aws_region}:{account}:{namespace}-EventBus"
    result = dict(
        namespace=namespace,
        aws_profile=aws_profile,
        aws_region=aws_region,
        event_bus_topic=event_bus_topic,
        session=session,
        whoami=whoami
    )
    log.info('All settings: ' + json.dumps(result, default=str))
    return result

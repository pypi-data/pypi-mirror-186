#!/usr/bin/env python3
import click
import click_log
import logging
from bdating_common import collect_default

log = logging.getLogger(__name__)
click_log.basic_config(log)

# This global info might be used with multiple threading enviroment.
# Think careful of concurrency.
global_info = {
  'session_info':None
} 
def _generate_dict(dimensions):
  result = []
  for kv in dimensions:
    key, value = kv.split('=', 1)
    result.append({
        'Name': key,
        'Value': value
    })

  return result


def _check_int(s:str):
  if s[0] in ('-', '+'):
    return s[1:].isdigit()
  return s.isdigit()

# @multi_threading.threaded
def report_metric(
    namespace: str,
    metric_name: str,
    value, # int or float
    unit: str = 'None',
    aws_profile: str = None,
    aws_region: str = None,
    dimensions: tuple = (),
    resolution: int = 60,
    logger = None
):
  """Report cloudwatch metrics.

  Args:
      namespace ([type], optional): [description].
      metric_name ([type], optional): [description].
      aws_profile ([type], optional): [description]. Defaults to None.
      aws_region ([type], optional): [description]. Defaults to None.
      value ([type], optional): [description].
      dimensions ([type], optional): [description]. Defaults to empty list.
      unit ([type], optional): [description]. Defaults to None. selection: 'Seconds' | 'Microseconds' | 'Milliseconds' | 'Bytes' | 'Kilobytes' | 'Megabytes' | 'Gigabytes' | 'Terabytes' | 'Bits' | 'Kilobits' | 'Megabits' | 'Gigabits' | 'Terabits' | 'Percent' | 'Count' | 'Bytes/Second' | 'Kilobytes/Second' | 'Megabytes/Second' | 'Gigabytes/Second' | 'Terabytes/Second' | 'Bits/Second' | 'Kilobits/Second' | 'Megabits/Second' | 'Gigabits/Second' | 'Terabits/Second' | 'Count/Second' | 'None',
  """
  global global_info
  if not global_info['session_info']:
    global_info['session_info'] = collect_default.collect_info_for_apps(
        aws_profile=aws_profile,
        aws_region=aws_region,
        logger=logger,
    )
  sys_info=global_info['session_info']
  client = sys_info['session'].client('cloudwatch', region_name=sys_info.get('aws_region'))
  if logger:
    logger.debug(f"Metrics to be put to namspace {namespace}, metric name {metric_name}, value {value}")
  client.put_metric_data(
      Namespace=namespace,
      MetricData=[
          {
              'MetricName': metric_name,
              'Dimensions': dimensions,
              # 'Timestamp': datetime.datetime.now(),
              'Value': value,
              'Unit': unit,
              'StorageResolution': resolution
          },
      ]
  )
  if logger:
    logger.info(f"Metrics put for namspace {namespace}, metric name {metric_name}, value {value}")

@click.command()
@click.option('--namespace', '-n', help='The namespace to report', required=True, default='Testing')
@click.option('--profile', '-p', help='The profile', default=None)
@click.option('--region', '-r', help='The AWS region', default='ap-southeast-2')
@click.option('--metric-name', '-m', help='Them metric name', default='Testing')
@click.option('--value', '-V', help='Them metric value', default='1')
@click.option('--unit', '-u', help='Them metric unit', default='None', type=click.Choice([
    'Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes',
    'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count',
    'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second',
    'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second',
    'Count/Second' , 'None',
],))
@click.option('--dimension', '-d', help='The Dimention to add. Format KEY=value.',
              default=[], multiple=True)
@click_log.simple_verbosity_option(log)
def report(namespace, profile, region, metric_name, value, unit, dimension):
  """Report a metric"""
  report_metric(
      namespace=namespace,
      aws_profile=profile,
      aws_region=region,
      metric_name=metric_name,
      value=int(value) if _check_int(value) else float(value),
      dimensions=_generate_dict(dimension),
      unit=unit,
      logger=log,
  )
  if not namespace == 'Testing' and not namespace.startswith('Sonder/'):
    namespace = f"Sonder/{namespace}"
  log.info(f"https://{region}.console.aws.amazon.com/cloudwatch/home?region={region}#metricsV2:graph=~(view~'timeSeries~stacked~false~region~'ap-southeast-2~stat~'Minimum~period~60);query=~'{namespace}")

if __name__ == '__main__':
  report()

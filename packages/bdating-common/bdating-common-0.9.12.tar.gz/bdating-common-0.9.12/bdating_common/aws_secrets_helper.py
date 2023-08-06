import boto3
from botocore.exceptions import ClientError
import json
import base64
import os

def get_secret(secret_name: str, logger=None) -> dict:
  session = boto3.session.Session()
  client = session.client(
      service_name='secretsmanager',
      region_name=os.environ.get('AWS_REGION', 'ap-southeast-2')
  )
  try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
  except ClientError as e:
    if logger:
      logger.error(f"Secret: {secret_name} failed, reason: {str(e)}")
    raise e
  else:
    if 'SecretString' in get_secret_value_response:
      secret = get_secret_value_response['SecretString']
    else:
      secret = base64.b64decode(get_secret_value_response['SecretBinary'])
  return json.loads(secret)

import json
import urllib3
from base64 import b64encode

http = urllib3.PoolManager()

def lambda_handler(event, context):

    message = json.loads(event['Records'][0]['Sns']['Message'])

    payload = {
        "data": {
            "AlarmName": message['AlarmName'],
            "State": message['NewStateValue'],
            "InstanceId": message['Trigger']['Dimensions'][0]['value']
        }
    }

    url = "https://instance-id.service-now.com/api/x_1687892_aws_in_0/aws_incident_api/create"

    username = "aws.integration"
    password = "#####password#####"

    credentials = b64encode(
        f"{username}:{password}".encode('utf-8')
    ).decode("ascii")

    response = http.request(
        "POST",
        url,
        body=json.dumps(payload),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Basic {credentials}"
        }
    )

    return {
        'statusCode': response.status,
        'body': response.data.decode('utf-8')
    }

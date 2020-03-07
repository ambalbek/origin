from datetime import datetime, timezone
import boto3
from botocore.exceptions import ClientError

AWS_EMAIL_REGION = 'us-east-1'
MAX_AGE = 1

iam=boto3.client('iam')

def lambda_handler(event, contex):
    paginator=iam.get_paginator('list_users')
    for responce in paginator.paginate():
        for user in responce['Users']:
            username=user['UserName']
            res=iam.list_access_key(UserName=user)
            for access_key in res['AccessKeyMetadata']:
                access_key_id=access_key['AccessKeyId']
                create_date = access_key['CreateDate']
                return(username, access_key_id ,create_date)
                age = days_old(create_date)
                if age >= MAX_AGE:
                    return access_key_id,access_key,age.days
                    
                #send_email_report(EMAIL_TO,username,access_key_id)
def days_old(create_date):
    now=datetime.now(timezone.utc)
    age =now - create_date
    return age.days
'''
def send_email_report(email_to, age, access_key_id):
    data = (f'Access Key {access_key_id} belonging to user {username} has been deactivated due to {age} days old.')
    try:
        responce=ses.send_email(
            Source=EMAIL_FROM,
            Destination={
                'ToAddresses':[EMAIL_TO]
            },
            Message={
                'Subject':{
                    'Data':('AWS IAM Access Key Rotation- Deactivation of'
                            f'Acess Keys: {access_key_id}')

                },
                'Body':{
                    'Text':{
                        'Data':data
                    }

                }
            })
    except:
        print(e.response['Error']['Message'])
'''


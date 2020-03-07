import datetime, boto3, csv, pandas as csv

IAM = boto3.client('iam')
def access_key(user):
    keydetails=IAM.list_access_keys(UserName=user)
    for keys in keydetails['AccessKeyMetadata']:
        if keys['Status']=='Active' and (time_diff1(keys['CreateDate']))>= 90:
            print (keys['UserName'],keys['AccessKeyId'], time_diff1(keys['CreateDate']),sep=',')
def time_diff1(keycreatedtime1):
    now=datetime.datetime.now(datetime.timezone.utc)
    diff=now-keycreatedtime1
    return diff.days


if __name__ == '__main__':
      
    details = IAM.get_account_authorization_details()
    print ("Username","AccessKey","KeyAge",sep=',')
    for user in details['UserDetailList']:
        access_key(user['UserName'])

    
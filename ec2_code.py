import boto3
 
AMI = 'ami-04902260ca3d33422'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'octoberkeypair'
REGION = 'us-east-1'
 
 
ec2 = boto3.client('ec2', region_name=REGION)
 
 
def lambda_handler(event, context):
 
    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MaxCount=1,
        MinCount=1
    )
    
    print ("New instance created:")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)
 
    return instance_id

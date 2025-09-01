import boto3

ec2 = boto3.client('ec2')

internet_gateway_id = 'igw-03ea7df7391ac7a2b'

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id
)
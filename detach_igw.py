import boto3

ec2 = boto3.client('ec2')

internet_gateway_id = 'igw-03ea7df7391ac7a2b'
vpc_id = 'vpc-07d748aec29d43fd9'

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id
)
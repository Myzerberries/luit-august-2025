import boto3

ec2 = boto3.client('ec2')

vpc_id = "vpc-07d748aec29d43fd9"

ec2.delete_vpc(
    VpcId=vpc_id
)
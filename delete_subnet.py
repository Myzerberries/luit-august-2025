import boto3

ec2 = boto3.client('ec2')

subnet_id = "subnet-0806a0c2dcca07c5d"

ec2.delete_subnet(
    SubnetId=subnet_id
)
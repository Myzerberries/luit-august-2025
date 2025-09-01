import boto3

cidrBlock = '12.0.1.0/24'
vpc_id = 'vpc-07d748aec29d43fd9'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidrBlock, VpcId=vpc_id)

print (subnet["Subnet"]["SubnetId"])
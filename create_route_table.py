import boto3

ec2 = boto3.client('ec2')

vpc_id = 'vpc-07d748aec29d43fd9'

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])
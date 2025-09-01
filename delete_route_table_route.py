import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-02a7850747c115ae6'

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id
)
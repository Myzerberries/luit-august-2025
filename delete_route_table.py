import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-02a7850747c115ae6'

ec2.delete_route_table(
    RouteTableId=route_table_id
)
import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-02a7850747c115ae6'
internet_gateway_id = 'igw-03ea7df7391ac7a2b'

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id
)
import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-02a7850747c115ae6'

response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id
    ]
)


for association in response["RouteTables"][0]["Associations"]:
    if not association["Main"]:
        association_id = association["RouteTableAssociationId"]
        print(association_id)
        ec2.disassociate_route_table(
            AssociationId=association_id
        )
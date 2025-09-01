import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-02a7850747c115ae6'

subnet_id = 'subnet-0806a0c2dcca07c5d'

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id
)

print (association["AssociationId"])
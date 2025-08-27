import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(

    Bucket='mlindle-boto3-08252025',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }

)

print (response)
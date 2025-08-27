import boto3

from list_objects_boto3 import list_object_keys


def delete_object(client, bucket, key):
    response = client.delete_object(
    Bucket=bucket,
    Key=key
)
    
    return response

def delete_objects(client, bucket, keys):

    objects = [{'Key': key} for key in keys]

    response = client.delete_objects (
    Bucket=bucket,
    Delete={
        'Objects': objects
    }

    )
    return response

def delete_objects_non_recursive(client, bucket, keys, prefix):
    keys = [key for key in keys if "/" not in key[len(prefix):]]
    objects = [{'Key': key} for key in keys]

    response = client.delete_objects (
    Bucket=bucket,
    Delete={
        'Objects': objects
    }

    )
    return response

if __name__ == '__main__':
    
    bucket = 'mlindle-boto3-08252025'
    #key = 'test_text.txt'

    s3 = boto3.client('s3')

    #keys = ['test_text_upload.txt']

    #for key in keys:
    #    delete_object(s3, bucket, key)

   # delete_objects(s3, bucket, keys)

    prefix = "folder/foldera/"

    keys = list_object_keys(s3, bucket, prefix=prefix)
    #print (keys)
    #keys = [key for key in keys if "/" not in key[len(prefix):]]
    #print (keys)
    #delete_objects(s3, bucket, keys)
    delete_objects_non_recursive(s3, bucket, keys, prefix)
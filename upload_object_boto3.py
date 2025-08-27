import boto3

s3 = boto3.client('s3')

#with open("testfile.txt", 'rb') as f:
#    s3.put_object(Bucket="mlindle-boto3-08252025", Key="test_text.txt", Body=f, 
#                  ContentType = "text/plain")


#s3.upload_file('testfile.txt', 'mlindle-boto3-08252025', 'test_text_upload.txt', 
#               ExtraArgs={'ContentType' : 'text/plain'})

s3.put_object(Bucket='mlindle-boto3-08252025',
              Key='folder/foldera/folder1/test_text_string.txt',
              Body="This is a McTest",
              ContentType='text/plain')
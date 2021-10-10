import os
import boto3

s3 = boto3.resource('s3',
    endpoint_url = 'https://s3.ap-northeast-1.wasabisys.com',
    aws_access_key_id = os.environ["WASABI_KEY"],
    aws_secret_access_key = os.environ["WASABI_SECRET"]
)

bucket = s3.Bucket('sabamiso')
with open("upload-test.txt", "w") as outfile:
    outfile.write("Hello S3!")
    
bucket.upload_file("upload-test.txt", "test.txt")

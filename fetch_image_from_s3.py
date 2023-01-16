import base64
import boto3


s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = "MyBucket"
    file_name = "mypic.jpg"
    fileObj = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = fileObj["Body"].read()
    # print 
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/jpg",
            "Content-Disposition": "attachment; filename={}".format(file_name)
        },
        "body": base64.b64encode(file_content),
        "isBase64Encoded": True
    }
    

import boto3

# Use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('YCF-00605.png', 'rb')
s3.Bucket('guiles-boto3-bucket-kadir').put_object(Key='YCF-00605.png', Body=data)

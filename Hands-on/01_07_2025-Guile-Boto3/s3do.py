import boto3

s3 = boto3.resource('s3')

bucket_name = 'guiles-boto3-bucket-kadir'
bucket = s3.Bucket(bucket_name)

# Tüm objeleri sil
bucket.objects.all().delete()
print(f"All objects in bucket {bucket_name} have been deleted.")
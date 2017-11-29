
from boto.s3.connection import S3Connection

conn = S3Connection()

bucket = conn.create_bucket('project-bucket-cs351-web')

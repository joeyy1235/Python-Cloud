import math,os
import sys
import boto
from filechunkio import FileChunkIO

print ("Connection is being established to S3 bucket")
# connect t s3
conn = boto.connect_s3()
bucket = conn.get_bucket('project-bucket-cs351-web')

print("Fetching Content")
# get file info
source_path = sys.argv[1] 
source_size = os.stat(source_path).st_size

mp = bucket.initiate_multipart_upload(os.path.basename(source_path))

chunk_size = 4000
chunk_count = int(math.ceil(source_size / float(chunk_size)))

print("Uploading........")
for i in range(chunk_count):
	offset = chunk_size *i
	bytes = min(chunk_size, source_size - offset)
	with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
		mp.upload_part_from_file(fp, part_num=i + 1)
mp.complete_upload()
print("Upload complete")

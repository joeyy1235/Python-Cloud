import boto
from boto.s3.key import Key
conn = boto.connect_s3('AKIAJUSJYT4C5CD77OPA','bl0Qd/nhAM14CWm/PpHrKkTKpZ/tZSCUy/bDAKJV')
bucket = conn.get_bucket('project-bucket-cs351-web')
file_list = bucket.list()
for name in file_list:
	key_string =  str(name.key)
	print key_string
for name in file_list:
	key_string = str(name.key)
	name.get_contents_to_filename(key_string)
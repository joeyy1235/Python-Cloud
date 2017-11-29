import boto
from boto.s3.key import Key
conn = boto.connect_s3()
bucket = conn.get_bucket('project-bucket-cs351-3')
file_list = bucket.list()
print "File List"
for name in file_list:
	key_string =  str(name.key)
	print key_string
	#name.get_contents_to_filename(key_string)
file_name = raw_input('Enter file name to download :- ')
for name in file_list:
	key_string = str(name.key)
	if key_string == file_name:
		name.get_contents_to_filename(key_string)
#k = Key(bucket)
#k.key = 'test.txt'
#k.set_contents_from_file('test.txt')
#k.get_contents_to_file('downloaf.txt')

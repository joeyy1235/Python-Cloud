import boto.ec2
import time

conn = boto.ec2.connect_to_region('us-east-2')

# Enhanced creation now with the addition of 'user_data'

user_data_script = """#!/bin/bash
cd home/ubuntu
mkdir hello
sudo apt-get update
sudo apt -y install python
sudo apt -y install python-pip
export LC_ALL=C
pip install boto
echo -e "import boto" >> extract.py
echo -e "from boto.s3.key import Key" >> extract.py
echo -e "conn = boto.connect_s3('AKIAJUSJYT4C5CD77OPA','bl0Qd/nhAM14CWm/PpHrKkTKpZ/tZSCUy/bDAKJV')" >> extract.py
echo -e "bucket = conn.get_bucket('project-bucket-cs351-web')" >> extract.py
sudo echo -e "file_list = bucket.list()" >> extract.py
sudo echo -e "for name in file_list:" >> extract.py
sudo echo -e "\tkey_string =  str(name.key)" >> extract.py
sudo echo -e "\tprint key_string" >> extract.py
sudo echo -e "for name in file_list:" >> extract.py
sudo echo -e "\tkey_string = str(name.key)" >> extract.py
sudo echo -e "\tname.get_contents_to_filename(key_string)" >>extract.py
python extract.py
sudo apt-get install apache2 -y
sudo systemctl enable apache2
sudo cp next.html /var/www/html
sudo cp index.html /var/www/html
sudo systemctl start apache2"""

# Red Hat Enterprise Linux 6.4 (ami-10547475)
new_reservation = conn.run_instances(
                        'ami-10547475',
                        key_name='abcd',
                        instance_type='t2.micro',
                        security_groups=['default'],
                        user_data=user_data_script)
print "New instance created."

# Add a Name to the instance, then loop to wait for it to be running.
instance = new_reservation.instances[0]
#conn.create_tags([instance.id], {"Name":"PyWebDev Example 3b"})
while instance.state == u'pending':
    print "Instance state: %s" % instance.state
    time.sleep(10)
    instance.update()

print "Instance state: %s" % instance.state
print "Public dns: %s" % instance.public_dns_name
 

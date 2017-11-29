import time
from boto import ec2

it = 't2.micro'
# it = 'm1.small'
ami = "ami-099fe766"
instance_name = "mynewInstance"
security_group="quicklaunch-0"
ec2c = ec2.connection.EC2Connection('AKIAJUSJYT4C5CD77OPA','bl0Qd/nhAM14CWm/PpHrKkTKpZ/tZSCUy/bDAKJV')

user_data = """
wont work on ubuntu
"""

r = ec2c.run_instances(ami, instance_type=it, key_name='rg-ghy', user_data=user_data, security_groups=['default'])

time.sleep(5)
i = r.instances[-1]

ec2c.create_tags([i.id], {"Name": instance_name})

print "waiting for AMI to start ..."
while not i.update() == 'running':
    print ".",
    time.sleep(2)

print " ... success!"
print i.ip_address

# print "associated elastic IP?"
# print ec2c.associate_address(i.id, elastic_ip)
conn = boto.ec2.connect_to_region("us-east-1",aws_access_key_id='AKIAJUSJYT4C5CD77OPA',aws_secret_access_key='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')
conn.run_instances(
        'ami-099fe766',
        key_name='rg-ghy',
        instance_type='t2.micro',
        security_groups=['default'])
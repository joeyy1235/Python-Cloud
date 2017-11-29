import boto.ec2
import paramiko

print("\n\n ||||| Amazon EC2 BOTO utility ||||")
print("\n NOTE: The Key/instance info has already been hardcoded in the script\n This script currently supports only a single instance\n")
x=0
x=int(input("Press 1 to connect to the Amazon EC2 Service: "))

#Connect to the AWS service
if(x==1):
 conn = boto.ec2.connect_to_region("us-west-2",aws_access_key_id="AKIAJUSJYT4C5CD77OPA",aws_secret_access_key="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") 
 print("Connection to EC2 service successful ")

else:
 exit()


print("\n Available instances: \n")

#Get the instance public dns and name for further use
try:
 reservations = conn.get_all_reservations()
 r = reservations[0].instances[0]
 print(r.public_dns_name)
 inst = str(r)
 inst=inst[9:]
 print(inst)

except:
 print("Could not get the instance info...Try again later")
 exit()

while(x!=0):

 print("Options: \n Press 1 to launch an instance \n Press 2 to start a stopped instance \n Press 3 to stop the instance \n Press 4 to terminate the instance \n Press 5 to connect to the instance and execute a command \n Press 0 to exit")
 x = int(input("Enter your choice: "))
#give VM image name, Keypair name ,type and the security group for ssh access
 if(x==1):
  try:
   conn.run_instances('ami-099fe766',key_name='rg-ghy',instance_type='t2.micro',security_groups=['rg-ec2'])
  except:
   print("error while launching the instance")

 elif(x==2):
  try:
   instances=conn.get_only_instances(instance_ids=[inst])
   instances[0].start()
   print("Instance started\n")
  except:
   print("Error while starting the instance")

 elif(x==3):
  try:
   print(inst)
   conn.stop_instances(instance_ids=[inst])
   print("Instance Stopped...this doesn't destroy EBS volumes\n")
  except:
   print("Error while stopping the instance")


 elif(x==4):
  try:
   conn.terminate_instances(instance_ids=[inst])
   print("Instance terminated\n")
  except:
   print("Error terminating the instance")

#configure paramiko with the key we generated earlier and execute a command
 elif(x==5):
   try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file('C:/python27/KeyPairEC2.pem')
    ssh.connect(r.public_dns_name,username='ec2-user',pkey=privkey)
    stdin, stdout, stderr = ssh.exec_command('echo "TEST"')
    stdin.flush()
    data = stdout.read().splitlines()
    for line in data:
     print line
    ssh.close()
   except:
    print("Error while executing the shell command on the instance")


 elif(x==0):
   print("Thanks for using the BOTO script")

 else: print("please enter valid input")
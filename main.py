from sys import argv
import boto3

script, filename = argv
#Change the profile name to your local .aws\config profile name.
session = boto3.Session(profile_name='default')
#Change the region accordingly.
ec2 = session.resource('ec2', region_name='ap-southeast-2')
target = open(filename, 'w')
i = ec2.instances.filter()
# If you want to filter the instances by tag, replace TAG_NAME and TAG_VALUE.
'''
Filters = [{'Name':'tag:TAG_NAME', 'Values':['TAG_VALUE']}
         ])
'''
count=0

for instance in i:
    count +=1
    for tag in instance.tags:       # Three tags added as an example.
        if tag['Key'] == 'Name':
            tag_a = (tag['Value'])
        if tag['Key'] == 'Name':
            tag_b = (tag['Value'])
        if tag['Key'] == 'Name':
        	tag_c = (tag['Value'])

    # Modify output to display your required data.
    output = count,'Name: {}, Owner: {}, Instance ID: {}, Instance Type: {}, Private IP Address: {}'.format(tag_a, tag_b, instance.id, 
        instance.instance_type, instance.private_ip_address) 
    output_2 = 'Total Instances: {}'.format(count) #Lists the total number of instances
    target.write(str(output)) 
    target.write("\n")
    
target.write(str(output_2))
target.close()
print ('Target copy is complete. Please open {} for further details').format(filename)
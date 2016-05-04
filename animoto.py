import boto.dynamodb
import os
import time
from boto.sqs.message import Message
//Accesing dynamoDB 
conn = boto.dynamodb.connect_to_region(
        'us-west-2',
        aws_access_key_id=os.environ['aws_access_key'],
        aws_secret_access_key=os.environ['aws_secret_access_key'])
conn.list_tables()
message_table_schema = conn.create_schema(
        hash_key_name='jobid',
        hash_key_proto_value=str,
    )
"""table = conn.create_table(
        name='final_111',
        schema=message_table_schema,
        read_units=10,
        write_units=10
    )"""
#print table
#print conn.list_tables()
//connecting to table
table = conn.get_table('DynamonDB')
import os
conf = {
  "sqs-access-key": "********",
  "sqs-secret-key": "********",
  "sqs-queue-name": "rejul",
  "sqs-region": "us-west-2",
  "sqs-path": "sqssend"
}
import boto.sqs
conn = boto.sqs.connect_to_region(
        conf.get('sqs-region'),
        aws_access_key_id               = conf.get('sqs-access-key'),
        aws_secret_access_key   = conf.get('sqs-secret-key')
)
//Creating the queue object
my_queue = conn.get_queue('rejul1')
reverse = conn.get_queue('reverse')
m =  my_queue.get_messages(1)
start = time.time()
f = open("url",'w')
count = 0
while (len(m) > 0):
	k = m[0].get_body()
	#print k
	l = k.split(':::')
	#print l[1]
	try:
#	   print l[0]
	   table.get_item(hash_key=l[0])
	except  boto.dynamodb.exceptions.DynamoDBKeyNotFoundError:
	//Pulling of SQS Messages
	   data={'value': l[1]}
	   m1=Message()
	   m1.set_body(k[0]+" "+"T")
	   reverse.write(m1)
	   item = table.new_item(hash_key = l[0],attrs=data)
	   item.put()
	   my_queue.delete_message(m[0])
#	   os.system(l[1])
	   f.write(l[1])
        m=my_queue.get_messages(1)
last = time.time()

f1 =  open("final_url",'r')
for i in f1:
	// Downloading the images
	wgeturl  = "wget" + " " + "-O" + " " + " " + "image" + str(count) + ".jpg" + " " + str(i) 
	print wgeturl
	count = count + 1
	os.system(wgeturl)
os.system("rm out.mp4")
// Creating images
os.system("ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' -c:v libx264 out.mp4")

print "Time of Execution"
print last - start

conf = {
  "sqs-access-key": os.environ['aws_access_key_id'],
  "sqs-secret-key": os.environ['aws_secret_access_key'],
  "sqs-queue-name": "rejul1",
  "sqs-region": "us-west-2",
  "sqs-path": "sqssend"
}

import boto.sqs
conn = boto.sqs.connect_to_region(
        conf.get('sqs-region'),
        aws_access_key_id               = conf.get('sqs-access-key'),
        aws_secret_access_key   = conf.get('sqs-secret-key')
)

q = conn.create_queue(conf.get('sqs-queue-name'))
revesve = conn.create_queue(conf.get("Reverse"))
print conn.get_all_queues()

#from boto.sqs.message import RawMessage
from boto.sqs.message import Message
m = Message()
fp = open('url','r')
count  = 1
for i in fp:
	print i
	str1 = str(count) + ":::" + str(i)
	m = Message()
	count =  count + 1
	m.set_body(str1)
	retval = q.write(m)
	print 'added message, got retval: %s' % retval
fp.close()
#rs = q.get_messages(4)
#print len(rs)
#print rs[0].get_body()
#print rs[1].get_body()
#print rs[2].get_body()
#print rs[3].get_body()
"""import time
for i in range(0,8000):
        for m in q.get_messages():
                print '%s: %s' % (m, m.get_body())
                q.delete_message(m)
        time.sleep(.1) """

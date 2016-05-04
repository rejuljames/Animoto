
Animoto: Distributed System to convert Images to Video using Amazon AWS
--------

Animoto is used to convert images into videos using a distributed system. I used Amazon AWS to make the clusters.  Basic working is, From Instagram we take image URL and we keep these URL as messages in Amazon SQS ( SQS is Queueing System in Amazon). The workers (data nodes if we are speaking in hadoop terms) will fetch these messages (URL) from SQS queue and download images.
Linux command line utility called FFMEG will convert images to video. We combine all the videos in worker to get a single video. 
To provide 100 percent efficiency SQS keep multiple copies of same messages. 
So workers might read same messages again and again. Inoder to overcome that, I kept a DynamoDB in between SQS and worker. 
So when worker picks a messages job from SQS they will update the DynamoDB with a unique message ID  to avoid duplicate fetching. 
When next worker comes it makes sure that URL which worker is taken is not already processed

Host Configuration
------------------
Server: Amazon AWS T2.Micro Instance<br />
Operating system: Ubuntu Trusty 14.04<br />
Processor:  Intel Xeon Processors 3.3 GHZ<br />
Memory: 512 MB<br />
Disk:10GB<br />
Kernel Version:3.13.0-74-generic<br />


Files
------------------
Instagram.py: Get Image URLS from Instagram and saves to File<br />
client.py: Read the URL file and push the URLS to Amazon SQS<br />
db.py: Create a DynamoDB Table<br />
Worker: Worker get messages from SQS queue and download the images and convert the images to Video<br />






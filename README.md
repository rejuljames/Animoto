
Animoto: Distributed System to convert Images to Video using Amazon AWS
--------

Animoto is a cloud-based service which produces video from images using a distributed system. The clusters are set up with Amazon AWS.  The software uses Instagram to take and store image URL as messages in the Amazon SQS (Queuing System).

The workers (data nodes in Hadoop) fetch messages from the SQS queue as images. The Linux command line utility, FFMEG converts images to video. The software then combines each video into a single video. 

To attain 100% efficiency, SQS stores multiple copies of the same message. To avoid redundancy, a DynamoDB is deployed between SQS and worker. As a message is picked from the SQS, the worker updates the DB with a unique message ID.The following worker will not pick up a message whose ID is already present in the DB. 

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






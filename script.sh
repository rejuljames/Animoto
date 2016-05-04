cat 16 | \
while read CMD; do
    scp -i master121.pem .ssh/authorized_keys ubuntu@$CMD:/home/ubuntu/.ssh/
#    scp  combined.py  ubuntu@$CMD:~ 
done

#!/bin/bash

sleep 10

# Start the webserver.
python /home/brum/repo/webhook.py >> /home/brum/repo/all.log 2>&1 &

# Start the ultrahook forwarder.
ultrahook -k 'DSOSXGcVFi8Mh1Fx7Fv6vn6Dg73JXQns' github 5000 >> /home/brum/repo/all.log 2>&1 &

# Start Brum!
python /home/brum/repo/start.py >> /home/brum/repo/all.log 2>&1 &

#!/bin/bash

# Start the webserver.
python /home/brum/webhook-incoming-http/server.py >> /home/brum/all.log 2>&1 &

# Start the ultrahook forwarder.
ultrahook -k 'DSOSXGcVFi8Mh1Fx7Fv6vn6Dg73JXQns' github 5000 >> /home/brum/all.log 2>&1 &

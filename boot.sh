#!/bin/bash
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum
# boot.sh

# We wait 20 seconds for the WiFi connection to be established.
sleep 20

# Start the webserver aka webhook and pipe the output to the logfile.
python /home/brum/repo/webhook.py >> /home/brum/repo/all.log 2>&1 &

# Start the ultrahook forwarder.
ultrahook -k 'DSOSXGcVFi8Mh1Fx7Fv6vn6Dg73JXQns' github 5000 >> /home/brum/repo/all.log 2>&1 &

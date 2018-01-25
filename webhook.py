#!/usr/bin/env python
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum
# webhook.py

import socket, os, config
from subprocess import call

# Configure the host and port for the socket listener.
HOST, PORT = 'localhost', 5000

# Go to the root of the brum repository.
os.chdir('/home/brum/repo')

# Start listening on a socket using the configuration from above.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print 'Listening on port ' + str(PORT) + ' ...'

while True:

    # Accept an incoming connection.
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)

    print request

    # Act on the request:
    response = ""

    # If this was a webhook call from GitHub, start the update
    # procedure.
    if ("POST /update" in request):

        print "[*] Starting Git update.."

        # Pull the latest version off of GitHub.
        call(["git", "pull", "https://brumpi:"+config.token()+"@github.com/lesander/brum.git"])
        call(["chmod", "+x", "/home/brum/repo/boot.sh"])
        call("kill -15 $(pgrep -f /home/brum/repo/start.py)", shell=True)
        #call("python /home/brum/repo/start.py &", shell=True)

        print "[*] Done updating!"
        response = "Update complete"

    # If this was a direction call from a client,
    # write the desired direction to file.
    if ("POST /destination" in request):

        print "[*] Incoming destination.."

        # Save the destination to disk.
        lines = request.split("\n")
        print lines
        destination = lines[0].replace('POST /destination/', '')
        destination = destination.replace(' HTTP/1.1\r', '')
        with open('destination.txt', 'w') as file:
            file.write(destination)

        # Return OK!
        response = "Saved destination, starting route."
        call("python /home/brum/repo/start.py >> /home/brum/repo/all.log &", shell=True)

    # If the status of BRUM was requested,
    # we return the status.
    if ("POST /status" in request):

        print "[*] Status requested"

        # Get the current status from disk and return it.
        file = open('status.txt', 'r')
        status = file.readlines()[0]

        print "[*] Status is " + str(status)
        response = status

    # Send our response.
    http_response = "\nHTTP/1.1 200 OK\n\n" + response
    client_connection.sendall(http_response)
    client_connection.close()

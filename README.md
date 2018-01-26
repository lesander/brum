# Pizza Delivery Robot (BRUM)



## Deployment Pipeline
Once an update has been deployed or committed to the master branch of this repository, the Raspberry Pi inside BRUM will receive an incoming webhook request (powered by [ultrahook.com](http://ultrahook.com)). The Pi will then fetch the latest version of the repository from GitHub using a simple `git pull`.

## Usage
The end-user navigates to [bestuurbrum.nl](https://bestuurbrum.nl) and is able to pick one of three different delivery locations. Once the user has confirmed their destination, BRUM will be on it's way and keep te user informed through the webapp.

## How it works
The BRUM robot is guided using black stripes on a white surface. It has been programmed to recognize various obstacles and crossings using only it's three infrared contrast sensors.

## Run script on startup
Assuming your user is `brum` and the repository is cloned to `repo` create the following file `/etc/network/if-up.d/wlan0-up` with the following content:

```sh
#!/bin/sh
# filename: wlan0-up

if [ "$IFACE" = wlan0 ]; then
  echo "wlan0 up" >> /home/brum/repo/all.log
  /home/brum/repo/boot.sh
fi
```
Add executing permissions with `sudo chmod +x /etc/network/if-up.d/wlan0-up`

## API Keys
The API keys used in this project are revoked and no longer being used and are thus safe to publish.

## License
This code is released under the MIT License.

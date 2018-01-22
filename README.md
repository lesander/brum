# brum

## Setting up the Pi
Assuming your user is `brum` and the repository is cloned to `repo` create the following file `/etc/network/if-up.d/wlan0-up `

```sh
#!/bin/sh
# filename: wlan0-up

if [ "$IFACE" = wlan0 ]; then
  echo "wlan0 up" >> /home/brum/repo/all.log
  /home/brum/repo/boot.sh
fi
```
Add executing permissions with `sudo chmod +x /etc/network/if-up.d/wlan0-up`

## creating symbolic links

```
 ln -s /home/radha/Documents/manager  manager1
```
### connect to wifi from terminal 
```
#!/usr/bin/env bash
echo "give wifi name"
#https://www.makeuseof.com/connect-to-wifi-with-nmcli/
read wifi_name
nmcli con up $wifi_name
echo "connecting"

```

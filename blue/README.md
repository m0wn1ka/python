https://gist.github.com/m0wn1ka/d8312ab6e4dd2f0e69579ba3e5ff0fb1
## main purpose(for linux users)
- check the security of our system
- whether there was any unauthoried accesss happended recenly
## expected output
- last login of user i.e log of recent user logins
- log of commands ran as sudo
- any open ports :nmap
- recently installed sofwares (by dpkg -i or sudo apt install)
- recently connected wifi details
- last run 10 commands 
- any changes to /etc/hosts file
- any changes to env variables(/etc/profile file)
- any thing in crontab
- any vpn connections
- see who have write access to /etc/shadow
- any usb connections
- any wget or curl
- any ssh connections
- earphones conections

- https://stackoverflow.com/questions/21762356/history-command-works-in-a-terminal-but-doesnt-when-written-as-a-bash-script

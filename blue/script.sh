#!/bin/bash
rm -rf results
mkdir results
cd results
set -o history
history -r ~/.bash_history
echo "last run 10 commands last_run_commands.txt">>log.txt
history|tail>last_run_commands.txt
echo 'last logged in users data in login_stats.txt'>>log.txt
last|head>login_stats.txt
echo 'users who are currently logged in'>>log.txt
last | head| grep 'logged in' >>log.txt
echo 'commands which were ran as sudo in sudo_cmds.txt'>>log.txt
history|grep 'sudo'|tail>sudo_cmds.txt
echo 'recently installed apps are in recently.text'>>log.txt
history|grep 'sudo apt install'> recently.txt
history|grep "dpkg -i" >>recently.txt
echo 'open ports status is in open_ports.txt'>>log.txt
nmap 127.0.0.1>open_ports.txt
echo 'all connected wifi devices in wifi_log.txt'>>log.txt
nmcli -f NAME con show >wifi_logs.txt
echo 'status of change of hosts file,password file,env variables in file_stat.txt'>>log.txt
stat /etc/hosts > file_stat.txt
stat /etc/passwd >>file_stat.txt
stat ~/.bashrc>>file_stat.txt
echo 'status of vpn is '>>log.txt
x=ifconfig|grep 'tun' -c >>log.txt
if [[ $x -ne 0 ]]
   then
       echo "a open vpn is found">>log.txt
   else
       echo "no open vpn is found">>log.txt
fi
echo 'see resUlts/log file '
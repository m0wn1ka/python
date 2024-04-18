import os
import subprocess

shell = "/bin/bash"
fp = open("result.txt", "w")

def assudo(x):
    return 'echo 1010|' + x

def shell_cmd(x):
    result = subprocess.run(x, shell=True, executable=shell, capture_output=True, text=True)
    return result

def login_status():
    cmd = 'last|head>login_status.txt'
    shell_cmd(cmd)
    cmd = "last | head| grep 'logged in' -c"
    result = shell_cmd(cmd)
    no_of_users = int(result.stdout)
    if no_of_users > 1:
        fp.write("more than one user currently logged in. See login_status.txt file\n")

def history_status():
    res = shell_cmd('echo $HISTFILE')
    if res.stderr:
        print("Error:", res.stderr)
    else:
        print("HISTFILE:", res.stdout)

# login_status()
history_status()

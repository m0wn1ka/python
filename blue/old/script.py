import os
import subprocess
shell = "/bin/bash"
# os.system("sudo echo $0")
fp=open("result.txt","w")
bash_history=open("/home/radha/.zsh_history","r").read()
def assudo(x):
    return 'echo 1010|'+x
def shell_cmd(x):
    result = subprocess.run(x, shell=True,executable=shell, capture_output=True, text=True)
    return result

def login_status():
    cmd='last|head>login_status.txt'
    # subprocess.run(cmd,shell=True)
    shell_cmd(cmd)
    cmd="last | head| grep 'logged in' -c"
    result=shell_cmd(cmd)
    no_of_users=int(result)
    if(no_of_users>1):
        fp.write("more than one user curretly logged in see login_status.txt file")


def sudo_status():
    # https://askubuntu.com/questions/358867/how-to-view-the-bash-history-file-via-command-line
    # echo $HISTFILE->/home/radha/.zsh_history
    pass

# login_status()
sudo_status()
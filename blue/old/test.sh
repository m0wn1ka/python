#!/bin/bash
# https://stackoverflow.com/questions/21762356/history-command-works-in-a-terminal-but-doesnt-when-written-as-a-bash-script
set -o history
history -r ~/.bash_history
echo "hi"
history
echo $SHELL
echo "hello"
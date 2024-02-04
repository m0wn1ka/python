import time
import os
a="""            ___                __ _         
            / _ \              /_ | |        
  _ __ ___ | | | |_      ___ __ | | | ____ _ 
 | '_ ` _ \| | | \ \ /\ / / '_ \| | |/ / _` |
 | | | | | | |_| |\ V  V /| | | | |   < (_| |
 |_| |_| |_|\___/  \_/\_/ |_| |_|_|_|\_\__,_|"""
print(a)
display="""
option1:add new task
option2:start a task
option3:end   a task
option4:quit  
"""
task_option=0
if(os.path.exists("todo.txt")):
    with open("todo.txt","r") as f:
        tasks=list(f.readline())
        task_start=list(f.readline())
        task_end=list(f.readline())
else:
    tasks=[]
    task_start=[]
    task_end=[]
while task_option!=4:
    print(display)
    task_option=int(input("choose a option"))
    if(task_option==1):
        task=input("give task to add")
        tasks.append(task)
        task_start.append(0)
        task_end.append(0)
        print("task added")
    if(task_option==2):
        print("these are the tasks \n",tasks)
        start_no=int(input("enter the no of task to start"))
        # x=time.time()
        # y=time.ctime(x)
        task_start[start_no]=str(time.ctime(time.time()))
        print("started timer")
    if(task_option==3):
        print("these are the tasks \n",tasks)
        end_no=int(input("enter the no of task to end"))
        task_end[end_no]=str(time.ctime(time.time()))
        print("ended timer")
for i in range(len(tasks)):
    print(tasks[i],":",task_start[i],"-",task_end[i])
print(type(tasks),type(task_start),type(task_end))
with open("todo.txt","a") as f:
        tasks=f.write(str(tasks))
        f.write("\n")
        task_start=f.write(str(task_start))
        f.write("\n")
        task_end=f.write(str(task_end))
        f.write("\n")
print("bye...")




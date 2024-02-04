import time
import os
import csv
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
rows=[]
no_of_rows=0
if(os.path.exists("todo.csv")):
    with open("todo.csv","r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            rows.append(row)
        no_of_rows=csvreader.line_num
else:
    with open("todo.csv","w") as f:
        
        pass
while task_option!=4:
    print(display)
    task_option=int(input("choose a option"))
    if(task_option==1):
        task=input("give task to add")
        no_of_rows+=1
        rows.append([no_of_rows,task,0,0])
        print("task added")
    if(task_option==2):
        print("these are the tasks \n")
        for row in rows:
            print(row)
        try:
            start_no=int(input("enter the no of task to start"))-1
            rows[start_no][2]=str(time.ctime(time.time()))
        except:
            print("dont try to break....")
            exit()

        # x=time.time()
        # y=time.ctime(x)
        # task_start[start_no]=str(time.ctime(time.time()))
        print("started timer")
    if(task_option==3):
        print("these are the tasks \n")
        for row in rows:
            print(row)
        try:
             
            end_no=int(input("enter the no of task to end"))-1
            rows[end_no][3]=str(time.ctime(time.time()))
        except:
            print("dont try to break....")
            exit()
    if(task_option>4 or task_option<1):
        print("dont try to break....")
        exit()

with open("todo.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(rows)
for row in rows:
     print(row)

print("bye...")




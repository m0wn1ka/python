#sort it
#take only first occurances
#save in output 
#remove these numbers from the array
#repeate the steps
a=[2,2,3,3]
a=[3,4,2,5,3]
a=[]
#2,3,4,5,
answer=[]
while len(a)>0:
    a.sort()
    loop_ans=[]
    remaining=[]
    for i in range(len(a)):
        if(len(loop_ans)<=0 or loop_ans[-1]!=a[i]):
            loop_ans.append(a[i])
        else:
            remaining.append(a[i])
    for i in range(len(loop_ans)):
        a.remove(loop_ans[i])
    answer+=loop_ans
    a=remaining
print("ans is",answer)
points=0
for i in range(1,len(answer)):
    if(answer[i]>answer[i-1]):
        points+=1
print("points are :",points)

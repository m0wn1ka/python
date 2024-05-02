import re
a=open("chat1.txt").read()
a=re.sub("\d*/\d*/\d*, \d*:\d* - ","",a)
a=re.sub("Radha:","",a)
print(a)

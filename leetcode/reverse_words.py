class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split()
        length=len(s)
        x=0
        while(x<length//2):
            temp=s[x]
            s[x]=s[length-1-x]
            s[length-1-x]=temp
            x+=1
        return "".join(s)
a=Solution()
b=a.reverseWords("  hello       world  ")
print(b)
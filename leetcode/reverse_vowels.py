class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        vowel_positions=[]
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_positions.append(i)
        x=0
        s=list(s)
        print("vowel positons are",vowel_positions)
        length=len(vowel_positions)
        while(x<length//2):
            pos1=vowel_positions[length-1-x]
            pos2=vowel_positions[x]
            temp=s[pos1]
            s[pos1]=s[pos2]
            s[pos2]=temp
            x+=1
        return "".join(s)

a=Solution()
print(a.reverseVowels("hello"))
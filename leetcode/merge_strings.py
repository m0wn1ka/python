class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        total=len1+len2
        x,i,j=0,0,0
        result=""
        while(x<total):
            print(x)
            print(result)
            if(i<len1):
                result+=(word1[i])
                i+=1
                x+=1
            if(j<len2):
                result+=(word2[j])
                x+=1
                j+=1
         
        return result

        

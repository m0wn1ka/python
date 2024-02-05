//gives a good result but not accepted 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #take the smallest element
        #try to repeate it to make str1
        #decrease its size by 1 each time  and repeat
        len1=len(str1)
        len2=len(str2)
        if(len1<len2):
            min_word=str1
            min_len=len1
            max_len=len2
            max_word=str2
        elif(len1>len2):

            min_word=str2
            min_len=len2
            max_len=len1
            max_word=str1
        else:
            if(str1==str2):
                return str1
            else:
                print("i am from lie 23")
                return ""
        for i in range(min_len,0,-1):
            if(max_len%i==0):
               times_to_repeat=int(max_len/i)
               if(max_word==min_word[0:i]*times_to_repeat):
                   return min_word[0:i]
            else:
                continue
            
        print("i am form ast")
        return ""

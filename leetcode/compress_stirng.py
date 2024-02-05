class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        new_array=[]
        new=False
        present=chars[0]
        present_count=1
        for i in range(1,len(chars)):
            if(chars[i]==present):
                present_count+=1
                if(i==len(chars)-1):
                    new_array.append(present)
                    new_array+=(list(str(present_count)))
            else:
                if(i==len(chars)-1):
                    new_array.append(present)
                    new_array.append(str(present_count))

                new_array.append(present)
                new_array+=list((str(present_count)))
                present=chars[i]
                present_count=1
        return new_array



a=Solution()
b=a.compress(["a","a","b","b","c","c","c"])
print(b)
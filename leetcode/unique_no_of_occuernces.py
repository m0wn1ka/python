class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ans_dict={}
        for i in arr:
            if i in ans_dict.keys():
                ans_dict[i]+=1
            else:
                ans_dict[i]=1
        # print(ans_dict)
        values=ans_dict.values()
        values_set=set(values)
        if(len(values)==len(values_set)):
            return True
        else:
            return False
a=Solution()
# b=a.uniqueOccurrences([1,2,2,1,1,3])
b=a.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
print(b)
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        len_nums=len(nums)
        r=len_nums-k
        average=[]
        for i in range(r):
            x=nums[i]+nums[i+1]+nums[i+2]+nums[i+3]
            x=x/4
            average.append(x)
        return max(average)
a=Solution()
b=a.findMaxAverage([1,12,-5,-6,50,3],4)
print(b)
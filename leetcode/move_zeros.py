class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_zero=0
        for i in nums:
            if (i==0):
                count_zero+=1
        ans=[]
        for i in range(len(nums)):
            if (nums[i]!=0):
                ans.append(nums[i])
        
        zeros=[0 for i in range(count_zero)]
        print(zeros)
        ans=ans+zeros
        return ans
a=Solution()
b=a.moveZeroes([0,1,0,3,12])
print(b)
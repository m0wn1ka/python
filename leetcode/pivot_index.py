class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for j in range(len(nums)):
            left_sum=0
            for i in range(0,j):
                left_sum+=nums[i]
            right_sum=0
            for i in range(j+1,len(nums)):
                right_sum+=nums[i]
            if(left_sum==right_sum):
                return j
        return -1
a=Solution()
# b=a.pivotIndex([1,7,3,6,5,6])
# b=a.pivotIndex([1,2,3])
b=a.pivotIndex([2,1,-1])

print(b)
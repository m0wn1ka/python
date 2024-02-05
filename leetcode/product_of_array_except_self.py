class Solution:
    def productExceptSelf(self, nums):
        ans=[]
        for i in range(len(nums)):
            new_array=nums.copy()
            new_array.remove(nums[i])
            x=1
            for j in new_array:
                x=x*j
            ans.append(x)
        return ans
a=Solution()
b=a.productExceptSelf([1,2,3,4])
print(b)
class Solution:
    def productExceptSelf(self, nums):
        #find positions of zeros/count of them
        #find the product of non zero elements
        #if there are more thatn 1 zero then 
            #for all append zero
        #if there is exaclty one zero element
            #for all elements do product//element 
            #for zero element write the product
        zero_count=0
        product=1
        ans=[]
        zero_pos=-1
        for i in range(len(nums)):
            if(nums[i]==0):
                zero_count+=1
                zero_pos=i
            else:
                product*=nums[i]
        if(zero_count>1):
            for i in range(len(nums)):
                ans.append(0)
        else:
            for i in range(len(nums)):
                if(i!=zero_pos):
                    ans.append(int(product/nums[i]))
                else:
                    ans.append(0)
        return ans



a=Solution()
b=a.productExceptSelf([1,2,3,4])
print(b)
    
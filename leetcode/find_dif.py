class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        dif1=[]
        for i in nums1:
            if (i not in nums2) and (i not in dif1):
                dif1.append(i)
        dif2=[]
        for i in nums2:
            if (i not in nums1) and (i not in dif2):
                dif2.append(i)
        return [dif1,dif2]
a=Solution()
b=a.findDifference([1,2,3,3],[1,1,2,2])
print(b)
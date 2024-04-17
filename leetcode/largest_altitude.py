class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=[0 for i in range(len(gain)+1)]
        for i in range(1,len(gain)+1):
            print(i)
            alt[i]=alt[i-1]+gain[i-1]
        print(alt)
        return max(alt)


a=Solution()
b=a.largestAltitude([-5,1,5,0,-7])
print(b)
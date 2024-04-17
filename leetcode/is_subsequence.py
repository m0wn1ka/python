class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len=len(s)
        s_pos=0
        if(s_len)<1:
            return True
        for i in t:
            if(s[s_pos]==i):
                s_pos+=1
                if(s_pos==s_len):
                    return True
        if(s_pos==s_len):
            return True
        else:
            return False

a=Solution()
# b=a.isSubsequence("abc","ahbgdc")
b=a.isSubsequence("axc","ahbgcdc")
print(b)
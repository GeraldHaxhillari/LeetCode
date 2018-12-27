class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        m=0
        
        if x<0:
            x = -x
            k = -1
        else:
            k = 1
            
        while x > 0:
            m = x % 10 + m * 10
            x = x / 10
            
        if m >= 2**31 or m < -2**31:
            return 0
        
        return k*m

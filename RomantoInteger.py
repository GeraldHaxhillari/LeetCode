class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        s = map(lambda t: roman_dict[t], s)
        num = s[0]
        for i in xrange(1,len(s)):
            last = s[i-1]
            if s[i] < last:
                num -= s[i]
            else:
                num += s[i]
        return num

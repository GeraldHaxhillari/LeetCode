class Solution(object):
    intMap = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = Solution.intMap
        r = ''
        for n in sorted(m.keys(), reverse=True):
            r += m[n] * (num//n)
            num %= n
        return r

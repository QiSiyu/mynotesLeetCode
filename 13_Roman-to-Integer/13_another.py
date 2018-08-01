# Another way, try two characters every time. Dealing with possible errors. Slower than mine
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1,'IV': 4,'V':5,'IX': 9,'X':10,'XL': 40,'L':50,'XC': 90,'C':100,'CD': 400,'D':500,'CM': 900,'M':1000}
        out = 0
        ii = 0
        while ii < len(s):
            try:
                out += dict[s[ii:ii+2]]
                ii += 2
            except (ValueError, KeyError):
                out += dict[s[ii]]
                ii += 1
        return out
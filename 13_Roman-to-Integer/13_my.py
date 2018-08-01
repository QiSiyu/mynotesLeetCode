# comparing adjacent value, then add/subtract
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        out = 0
        for ii in range(len(s)-1):
            if dict[s[ii]] < dict[s[ii+1]]:
                out -= dict[s[ii]]
            else:
                out += dict[s[ii]]
        return out + dict[s[-1]]
        
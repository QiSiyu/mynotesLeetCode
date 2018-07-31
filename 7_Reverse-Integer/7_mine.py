# Used string for inversion. If using C++ or Java, the '%' operator is different and a digit-by-digit algorithm can be designed by applying %10 to x every time.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num_sign = x and (-1,1)[x>0]
        reversed_num = num_sign * int(str(abs(x))[::-1])
        if (reversed_num > 2**31 - 1) or (reversed_num < -2**31):
            reversed_num = 0
        return reversed_num
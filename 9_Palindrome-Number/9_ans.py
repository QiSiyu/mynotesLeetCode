# reverse half of the integer, compare with the other half. But need to eliminate exceptions: negative int or multiplies of 10 (IMPORTANT: will lead to wrong answer if not eliminated!)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        num1 = 0
        while x > num1:
            num1 = num1 * 10 + x % 10
            x = x/10
        return (x==num1) or (x == num1/10)
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rom = ''
        num_to_rom = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        numbers = list(num_to_rom.keys())
        numbers.sort()
        for ii in range(len(numbers)-1,-1,-1):
            rom += num_to_rom[numbers[ii]]*(num/numbers[ii])
            num = num%numbers[ii]
        return rom
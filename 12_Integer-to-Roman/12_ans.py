# simple solution, create lists for each possible combinations
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M_rom = ['','M','MM','MMM']
        C_rom = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        X_rom = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        I_rom = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        return M_rom[num/1000] + C_rom[(num%1000)/100] + X_rom[(num%100)/10] + I_rom[(num%10)]
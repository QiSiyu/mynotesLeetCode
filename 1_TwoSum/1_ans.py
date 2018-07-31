# O(n) method, loops over the list only once.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        adder_dict = {}
        for ii in range(len(nums)):
            if nums[ii] in adder_dict:
                return [adder_dict[nums[ii]], ii]
            else:
                adder_dict[target - nums[ii]] = ii
        return
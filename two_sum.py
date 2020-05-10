class Solution(object):
    def twoSum(self, nums, target):
        a = {}
        for i, j in enumerate(nums):
            if target-j in a:
                return [a[target-j],i]
            else:
                a[j] = i
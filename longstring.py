class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlen = curlen = 0
        for i, val in enumerate(s):
            if val in dicts:
                sum = dicts[val] + 1
                if sum > curlen:
                    curlen = sum
            num = i - curlen + 1
            if num > maxlen:
                maxlen = num
            dicts[val] = i
        return maxlen

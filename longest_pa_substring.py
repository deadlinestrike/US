class Solution:
    def longestPalindrome(self, s):
        maximum = ""
        temp = ""
        for index in range(len(s)):
            if len(maximum) >= len(s) - index:
                break
            for index2 in range(index+len(maximum),len(s)+1):
                fw = s[index:index2]
                bw = fw[::-1]
                if fw == bw:
                    temp = fw
                    if len(temp) > len(maximum):
                        maximum = temp
        return maximum
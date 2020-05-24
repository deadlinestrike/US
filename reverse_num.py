class Solution:
    def reverse(self, x):
        if x > 0:
            a = int(str(x)[::-1])
        if x <= 0:
            a = -1 * int(str(x * -1)[::-1])
        min = -2 ** 31
        max = 2 ** 31 - 1
        if a not in range(min, max):
            return 0
        else:
            return a
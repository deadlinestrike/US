class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        a = len(s)
        cycle = 2 * numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, a, cycle):
                strlist.append(s[j])
                if i != numRows - 1 and i != 0 and j + cycle - 2 * i < a:
                    strlist.append(s[j + cycle - 2 * i])
        final = ''.join(strlist)
        return final

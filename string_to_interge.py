class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # 去除空格
        if len(s) == 0:  # 判断是否为空
            return 0
        if s[0] not in "-+" and not s[0].isdigit():  # 判断是否有数字字符
            return 0
        num = ""
        isDigit = False
        for ch in s:  # 将所有数字字符放入num字典
            if isDigit and not ch.isdigit():
                break
            if ch in "-+" or ch.isdigit():
                num += ch
                isDigit = True

        a = 1
        if num[0] in "-+":  # 将+-字符放在首位
            if num[0] == "-":
                a = -1
            num = num[1:]

        res = 0
        for ch in num:  # 逐个输出各个数字
            res *= 10
            res += ord(ch) - ord("0")  # 将字符转换为数字
        return max(-2 ** 31, min(res * a, 2 ** 31 - 1))  # 限制界限

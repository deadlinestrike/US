class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i1 = 0
        i2 = 0
        num1 = 0
        num2 = 0 #初始化
        len1 = len(nums1)
        len2 = len(nums2)
        len4 = len1 + len2
        len3 = int(len4 / 2) + 1 #获取中间值
        for x in range(len3):
            if len1 > i1 and len2 > i2: #两个列表都不为空
                if nums1[i1] <= nums2[i2]: #排序
                    num1 = num2
                    num2 = nums1[i1]
                    i1 = i1 + 1
                else:
                    num1 = num2
                    num2 = nums2[i2]
                    i2 = i2 + 1
            elif len1 > i1: #列表一不为空
                num1 = num2
                num2 = nums1[i1]
                i1 = i1 + 1
            else: #列表二不为空
                num1 = num2
                num2 = nums2[i2]
                i2 = i2 + 1

        if len4 % 2 == 0: #数组元素个数为偶数取中间两数和除2
            return (num1 + num2) / 2
        else: #奇数取中值
            return float(num2)
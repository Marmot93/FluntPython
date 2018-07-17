# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 10:21 AM
# @Author  : Marmot
# @File    : 7_翻转整数.py


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x < 0:
            flag = True
        x = ''.join([_ for _ in str(x)[::-1]])
        if flag:
            s = int('-' + x[:-1])
            return s if s > -2 ** 31 else 0
        return int(x) if int(x) < 2 ** 31 else 0


print(Solution().reverse(-123))

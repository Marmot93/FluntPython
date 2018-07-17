# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 6:12 PM
# @Author  : Marmot
# @File    : 326_3的幂.py


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        num = 3 ** i
        while n != num:
            if n < num:
                return False
            else:
                i += 1
                num = 3 ** i
        return True

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
        while n % 3 == 0 and n > 1:
            n = n / 3
        if n == 1:
            return True
        else:
            return False

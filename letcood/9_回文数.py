# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 10:55 AM
# @Author  : Marmot
# @File    : 9_回文数.py


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

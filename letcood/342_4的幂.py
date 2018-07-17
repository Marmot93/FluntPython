# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 6:16 PM
# @Author  : Marmot
# @File    : 342_4的幂.py


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return bin(num).replace("00", '') == '0b1'

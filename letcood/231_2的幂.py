# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 5:36 PM
# @Author  : Marmot
# @File    : 231_2的幂.py


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # i = 0
        # num = 2 ** i
        # while n != num:
        #     if n < num:
        #         return False
        #     else:
        #         i += 1
        #         num = 2 ** i
        # return True
        if n < 0:
            return False
        return bin(n).count("1") == 1


print(Solution().isPowerOfTwo(1))

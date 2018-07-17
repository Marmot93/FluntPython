# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 4:39 PM
# @Author  : Marmot
# @File    : 66_加一.py


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = int(''.join([str(_) for _ in digits])) + 1
        l = []
        while s // 10 > 0:
            s, y = divmod(s, 10)
            l.insert(0, y)
        l.insert(0, s)
        return l


print(Solution().plusOne([4, 3, 2, 9]))

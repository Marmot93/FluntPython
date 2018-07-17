# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 5:10 PM
# @Author  : Marmot
# @File    : 374_猜数字.py


def guess(num):
    my = 2
    if my < num:
        return -1
    elif my > num:
        return 1
    else:
        return 0


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = (start + end) // 2
        while guess(mid) != 0:
            if guess(mid) == -1:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return mid


print(Solution().guessNumber(2))

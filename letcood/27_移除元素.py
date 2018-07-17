# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 4:31 PM
# @Author  : Marmot
# @File    : 27_移除元素.py


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            del nums[nums.index(val)]
            self.removeElement(nums, val)
        except ValueError:
            return len(nums)

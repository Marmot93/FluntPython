# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 6:07 PM
# @Author  : Marmot
# @File    : 两数之和.py


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

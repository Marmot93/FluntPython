# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 12:04 PM
# @Author  : Marmot
# @File    : 14_最长公共前缀.py


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        i = 0
        while True:
            try:
                tmp = strs[0][i]
                for item in strs:
                    if item[i] != tmp:
                        return prefix
            except IndexError:
                return prefix
            prefix += tmp
            i += 1
        return prefix

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        for _, item in enumerate(zip(*strs)):
            if len(set(item)) > 1:
                return prefix
            else:
                prefix += item[0]
        return prefix


print(Solution().longestCommonPrefix(["c", "c"]))

# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 11:02 AM
# @Author  : Marmot
# @File    : 13_罗马数字转整数.py


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        # 反向操作
        for i in range(len(s) - 1):
            if map[s[i]] < map[s[i + 1]]:
                sum -= map[s[i]]
                continue
            sum += map[s[i]]
        return sum + map[s[-1]]


print(Solution().romanToInt("MCMXCIV"))

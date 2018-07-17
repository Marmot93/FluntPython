# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 5:01 PM
# @Author  : Marmot
# @File    : 412_FizzBuzz.py


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['1']
        l = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                l.append('FizzBuzz')
            elif i % 3 == 0:
                l.append('Fizz')
            elif i % 5 == 0:
                l.append('Buzz')
            else:
                l.append(str(i))
        return l

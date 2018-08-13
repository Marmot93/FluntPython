# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 6:10 PM
# @Author  : Marmot
# @File    : ceshi.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_sum(l1, num=None):
    if num is None:
        num = []
    num.append(l1.val)
    if l1.next:
        get_sum(l1.next, num)
    else:
        return sum(num)


def prodcut_L(ln, val, next):
    ln.val = val
    ln.next = ListNode(next)
    return ln


def f(ln, l, next):
    for i in l:
        if i is None:
            return ln
        else:
            f(prodcut_L(ln, i, next), i, next)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = get_sum(l1)
        sum2 = get_sum(l2)
        sum3 = [int(_) for _ in str(sum1 + sum2)]
        sum3.reverse()
        l = len(sum3)

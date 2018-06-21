# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 下午5:06
# @Author  : Marmot
# @File    : generators.py

import itertools

# Generators are iterators, a kind of iterable you can only iterate over once.
from pprint import pprint

gen = (i for i in range(10))
for i in gen:
    print(1, i)
for i in gen:
    print(2, i)
print(type(gen))


def createGenerator():
    mylist = range(10)
    for i in mylist:
        yield i


x = createGenerator()
for i in x:
    print(3, i)
for i in x:
    print(4, i)

print(type(x))

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
pprint(list(races))

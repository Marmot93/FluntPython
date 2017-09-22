"""format 笔记"""

# 字典格式化
d = {'one': 1, 'two': 2}
# format key
print('{}, {}'.format(*d))
# format value
print('{one}, {two}'.format(**d))

# 列表格式化
l = [1, 2]
print('l: {}, {}'.format(*l))
# 通过下标
print('l: {0[1]}, {0[0]}'.format(l))

# tuple 格式化
t = (1, 2)
print('t: {}, {}'.format(*t))

# set 格式化
s = {1, 2}
print('s: {}, {}'.format(*s))

# 位置格式化 :(占位符)(<, ^, >,)(位数)
sting = 'string'
print('{:<10}左对齐'.format(sting))
print('{:^10}居中'.format(sting))
print('{:>10}右对齐'.format(sting))
print('{:*>10}*占位右对齐'.format(sting))

# 精度格式化 :.(ndigits)f
print('{:.2f}'.format(321.33345))

# 千位分隔符 ：，
print('千位分隔符：{:,}'.format(1234567890))

# 二进制 b
print('二进制：{:b}'.format(16))
# 八进制 d
print('八进制：{:d}'.format(16))
# 十进制 o
print('十进制：{:o}'.format(16))
# 十六进制 x
print('十六进制：{:x}'.format(16))

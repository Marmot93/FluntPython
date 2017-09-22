from difflib import SequenceMatcher, Differ

# SequenceMatcher
# 对比字符串
A = "private Thread currentThread;"
B = "private volatile Thread currentThread;"
s = SequenceMatcher(lambda x: x == " ", A, B)
# 相似度
print('相似度', round(s.ratio(), 3))

# 最长匹配 find_longest_match(A起, A末, B起, B末) = Match(A起, B起, 最大长度)
print('\n最长匹配', s.find_longest_match(0, len(A), 0, len(B)))

# 分块对比
print('\n分块对比')
for block in s.get_matching_blocks():
    # block = Match(a=29, b=38, size=0)
    # print("a[%d] and b[%d] match for %d elements" % block)
    print("a[{}] and b[{}] match for {} elements".format(*block))

# 块对比
print('\n块对比')
for opcode in s.get_opcodes():
    # opcode = ('equal', 8, 29, 17, 38)
    # print("%6s a[%d:%d] b[%d:%d]" % opcode)
    print("{:<8} a[{}:{}] b[{}:{}]".format(*opcode))

# Differ
# 字符串列表对比
print('\n字符串列表对比')
text1_l = "privat Thread currentThread;".split()
text2_l = "private volatile Thread currentThread;".split()
d = Differ()
# 传入两个字符串列表
diff = d.compare(text1_l, text2_l)
print('\n'.join(diff))

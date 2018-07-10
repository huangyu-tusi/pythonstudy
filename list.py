l1 = [1, 2, 3, 4, 5, 3]
l2 = ['one', 'two', 'three', 'four', 'five','two']
l3 = [1, 'tow', 3, 'tow']
l4 = list()
l5 = [1, 3, 4, [10, 20]]
'''for i in range(len(l1)):
    print(l1[i])
'''
l1[1] = 10
print("列表原始大小：%d" % len(l1))
# 追加元素
# l1 = l1 + [6, 7, 8]
# l1.append(6)
# l1.extend([6, 7, 8])

# 插入元素
l1.insert(2, 8)
print("列表现在的大小 %d" % len(l1))
for x in l1:
    print(x)
# 统计元素出现次数
# print(l1.count(2))
# 判断指定元素是否存在于列表中
# print("www" in l2)
# 返回指定元素在列表中的索引值
# print(l2.index("onewww"))

# del l3[2], l3[1]
# l3.remove('tow')
# l3.pop()
l2.pop(1)
print(l2)

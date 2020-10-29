# 写代码，有如下字典，按照要求实现每一个功能
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

# 1、请循环遍历出所有的key
# for key in dic:
#     print(key)

# 2、请循环遍历出所有的value
# for key in dic:
#     print(dic[key])

# 3、请循环遍历出所有的key和value
# for key in dic:
#     print("字典dic中的key:", key)
#     print("对应的value：", dic[key])

# 4、请在字典中添加一个键值对，'k4':'v4'，输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)

# 5、请删除字典中的键值对，'k1':'v1'，并输出删除后的字典
# del dic['k1']
# print(dic)

# 6、请删除字典中的键'k5'对应的键值对，如果字典中不存在键'k5'，则不报错，并让其返回None
# if 'k5' in dic:
#     del dic['k5']
#     print(dic)
# else:
#     print(dic.get('k5'))

# 7、请获取字典中'k2'对应的值
# if 'k2' in dic:
#     print(dic.get('k2'))
#     # 或
#     print(dic['k2'])
# else:
#     print("不存在该键")

# 8、请获取字典中'k6'对应的值，如果键'k6'不存在，则不报错，并且让其返回None
# if 'k6' in dic:
#     print(dic['k6'])
# else:
#     print(dic.get('k6'))
# 或：
# print(dic.get('k6'))

# 9、现有dic2 ={'k1': 'v111', 'a': 'b'}通过一行操作使dic2 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'a': 'b'}
# dic2 ={'k1': 'v111', 'a': 'b'}
# dic2.update(dic)
# print(dic2)

# 10、组合嵌套题。写代码，有如下列表，按照要求实现每一个功能
lis = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
# 1.将列表list中的'tt'变成大写（用两种方式）
#   第一种：
#   lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].upper()
#   第二种：
#   lis[0][1][2]['k1'][0] = lis[0][1][2]['k1'][0].swapcase()

# 2.将列表中的数字3变成字符串'100'（用两种方式）
#   第一种：
# lis[0][1][2]['k1'][1] = '100'
#   第二种：
# lis1 = lis[0][1][2]['k1']
# lis2 = ['100' if x == 3 else x for x in lis1]
# lis[0][1][2]['k1'] = lis2

# 3.将列表中的字符串'1'变成数字101（用两种方式）
#   第一种：
# lis[0][1][2]['k1'][2] = 101
#   第二种：
# lis1 = lis[0][1][2]['k1']
# lis2 = [101 if x == '1' else x for x in lis1]
# lis[0][1][2]['k1'] = lis2
# print(lis)

# 11、按照要求实现以下功能：
#   现有一个列表 li = [1, 2, 3, 'a', 'b', 4, 'c']，有一个字典（此字典是动态生成的，你并不知道它里面有多少键值对，所以用dic = {}
# 模拟此字典）；现在需要完成这样的操作：如果该字典中没有'k1'这个键，那就创建这个'k1'键和其对应的值（该键对应的值设置为空列表），
# 并将列表li中的索引位为奇数对应的元素，添加到'k1'这个键对应的空列表中。如果该字典中有'k1'这个键，且'k1'对应的value是列表类型，那
# 就将列表li中的索引位为奇数对应的元素，添加到'k1'这个键对应的值中。
li = [1, 2, 3, 'a', 'b', 4, 'c']
dic = {}

if 'k1' in dic:
    if dic['k1'] == {}:
        dic['k1'] = li[::2]
else:
    dic.setdefault('k1', li[::2])

print(dic)
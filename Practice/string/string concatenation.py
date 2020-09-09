# 字符串拼接的几种方式

# 1、来自C语言的%方法
print('%s %s' % ('hello', 'world'))

# 2、format()拼接方式
# 简洁版
s1 = 'Hello {}! My name is {}.'.format('World', 'Python猫')
print(s1)
# >>>Hello World! My name is Python猫.
# 对号入座版
s2 = 'Hello {0}! My name is {1}.'.format('World', 'Python猫')
s3 = 'Hello {name1}! My name is {name2}.'.format(name1='World', name2='Python猫')
print(s2)
# >>>Hello World! My name is Python猫.
print(s3)
# >>>Hello World! My name is Python猫.

# 3、()类似元组方式
s_tuple = ('Hello', ' ', 'world')
s_like_tuple = ('Hello' ' ' 'world')

print(s_tuple)
# >>>('Hello', ' ', 'world')
print(s_like_tuple)
# >>>Hello world

print(type(s_like_tuple))
# >>><class 'str'>

# 4、面向对象模块拼接
from string import Template
s = Template('${s1} ${s2}!')
print(s.safe_substitute(s1='Hello',s2='world'))
# >>> Hello world!

# 5、常用的+符号
str_1 = 'Hello world! '
str_2 = 'My name is Python猫.'
print(str_1 + str_2)
# >>>Hello world！ My name is Python猫.
print(str_1)
# >>>Hello world！

# 6、join()方式拼接
str_list = ['Hello', 'world']
str_join1 = ' '.join(str_list)
str_join2 = '-'.join(str_list)
# print(str_join1) >>>Hello world
# print(str_join2) >>>Hello-world

# 7、f-sting方式
name = 'world'
myname = 'python_cat'
words = f'Hello {name}. My name is {myname}.'
print(words)
# >>> Hello world. My name is python_cat.
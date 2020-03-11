### 实用的Python代码小技巧

#### 1、重复元素判定

根据给定的列表，查找是否存在重复元素

```python
# set() 函数用于移除重复元素
def all_unique(list):
    return len(list) == len(set(list))

x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
all_unique(x) # False
all_unique(y) # True
```

#### 2、字符元素组成判定

检查两个字符串的组成元素是否一样

```python
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb") # True
```

#### 3、内存占用

```python
# 检查变量 variable 所占用的内存
import sys

variable = 30

print(sys.getsizeof(variable)) # 24
```

#### 4、字节占用

```python
# 检查字符串所占用的字节数
def byte_size(string):
    return(len(string.encode('utf-8')))

byte-size('Hello World') # 11
```

#### 5、打印 N 次字符串

```python
# 不采用循环语句的方法来打印 N 次字符串
n = 2
s = "Programming"

print(s * n) # ProgrammingProgramming
```

#### 6、大写第一个字母

```python
# 使用 title()方法，大写字符串中每一个单词的首字母
s = "programming is awesome"

print(s.title()) # Programming Is Awesome
```

#### 7、分块

```python
# 给定具体的大小，定义一个函数以按照这个大小切割列表
from math import ceil

def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size], list(lange(0, ceil(len(lst) / size)))))

chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], 5]
```

#### 8、压缩

```python
# 使用 filter()函数进行压缩，此方法可将布尔型的值去掉。
def compact(lst):
    return list(filter(bool, lst))

compact([0, 1, False, 2, '', 3, 'a', 's', 34])  # [1, 2, 3, 'a', 's', 34]
```

#### 9、解包

```python
# 可将打包好的成对列表解开成两组不同的元组
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)

print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]
```

#### 10、链式对比

```python
# 可在一行代码中使用不同的运算符对比多个不同的元素
a = 3
print(2 < a < 8) # True
pring(1 == a < 2) # False
```

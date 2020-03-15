#### 1、交换变量

```python
a = 3
b = 6
a, b = b, a

print(a) # 6
print(b) # 3
```

#### 2、字典推导（Dictionary comprehensions）和集合推导（Set comprehensions）

列表推导（List comprehensions）：

```python
some_list = [1, 2, 3, 4, 5]
another_list = [x + 1 for x in some_list]
print(another_list) # [2, 3, 4, 5, 6]
```

自 Python 3.1 开始，我们也可以用同样的语法来创建集合和字典表：

```python
# 字典推导（创建一个 key 是不重复的 1 到 10 之间的整数，value 是布尔型，用来指示 key 是否为偶数的字典）
d = {x: x % 2 == 0 for x in range(1, 11)}
print(d) # {1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False, 10: True}

# 集合推导（创建一个不含重复元素的偶数集合）
some_list = [1, 2, 3, 4, 5, 2, 1, 4, 8]
event_set = {x for x in some_list if x % 2 == 0}
print(event_set) # set([8, 2, 4])
```

#### 3、计数时使用 Counter 计数对象

```python
# 使用 Python 的 collections 类库中内置的 dict 类的子类 Counter
from collections import Counter
c = Counter('hello world')

print(c) # Counter({'1': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
print(c.most_common(2)) # [('1', 3), ('o', 2)]
```

#### 4、打印优雅的 JSON

使用 Python 内置的 json 处理，可以使 JSON 串具有一定的可读性，但当处理大型数据时，其表现为一个很长的、连续的一行，可读性差。
为了让 JSON 数据表现的更友好，可以使用 indent 参数来输出 JSON。这再控制台交互式编程或做日志时，尤为有用，同样也可使用内置的 pprint 模块来打印：

```python
import json
print(json.dumps(data)) # No indention
# {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, "name": "Joe", "lactose_intolerant": flase}]}
print(json.dumps(data, indent = 2)) # With indention
# {
#   "status": "OK",
#   "count": 2,
#   "results": [
#     {
#       "age": 27，
#       "name": "Oz"，
#       "lactose_intolerant": true
#     }，
#     {
#       "age": 29,
#       "name": "Joe",
#       "lactose_intolerant": flase
#     }
#   ]
# }
```

#### 5、解决 FizzBuzz 问题

```text
写一个程序，打印数字 1 到 100，3 的倍数打印“Fizz”来替换这个数，5 的倍数打印“Buzz”，
对于既是 3 的倍数又是 5 的倍数的数字打印“FizzBuzz”。
```

```python
for x in range(1, 101):
    print "fizz"[x % 3 * len('fizz')::] + "buzz"[x % 5 * len('buzz')::] or x
```

#### 6、if 语句在行内

```python
print "hello" if True else "world" # hello
```

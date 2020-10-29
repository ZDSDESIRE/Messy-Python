'''
37. 反转一个3位整数

反转一个只有3位数的整数。

样例 1:
  输入: number = 123
  输出: 321
样例 2:
  输入: number = 900
  输出: 9

注意事项
  你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000。

解决思路
  将整数转换为字符串，如果长度为1，则直接返回；
  通过三元表达式判断，如果字符串首字符不是符号(-/+)，则直接进行反转；如果字符串首字符是符号(-/+)，则将不含符号的字符串进行反转，删除开头的o字符，再与符号进行拼接。
  将反转后的字符串转换为整数值，通过三元表达式判断，如果整数值是32 位的整数，则直接返回，否则返回0。
'''

def get_reversed_int(x):
    x = str(x)
    if len(x) == 1:
        return x

    r = ''.join(reversed(x)) if x[0] not in ('-', '+') else x[0] + ''.join(reversed(x[1:])).lstrip('0')
    r = int(r) if -2**31 <= int(r) <= 2**31 - 1 else 0
    return r 

x = -12300
print(get_reversed_int(x))
-321

# class Solution:
#     """
#     @param number: A 3-digit number.
#     @return: Reversed number.
#     """
#     def reverseInteger(self, number):
#         # write your code here
        
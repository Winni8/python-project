# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/6 8:28
# @File 	:数据类型之间的转换.py
# @Software :PyCharm

import string, os

# TODO: str list tuple dict int float数据类型的相互转化：
# ==============================================
# 1、TODO str 与 list 之间的转换：
s = "www.baidu.com"

# 字符串转化成list，使用split()方法，进行拆分，转化成需要的列表形式
# 注意一点：split()经常与strip（）共同使用，strip（）表示：移除字符串头尾指定的字符
n = "mmmmmmmmmmmmsdfsdf.dgdgd.dgd.mmmmm"
n1 = n.strip("m")  # n1 = 'sdfsdf.dgdgd.dgd.'

a = s.split(" ")    # a =  ['www.baidu.com']
a1 = s.split(".", "n")  # a1 =['www', 'baidu.com'],"."表示去(.)并且在此处进行断点拆分，n 表示拆分次数；分成n+1段；
a2 = s.split(".", -1)  # a2 = ['www', 'baidu', 'com']  -1表示拆成最大段数

# 将list转成字符串，使用join（）方法
b = "".join(a)    # b = 'www.baidu.com'

# ==============================================
# 2、TODO str 与 int 之间的转换：
# 这个比较简单
s1 = "123456789"
int1 = int(s1)

int2 = 123654987
s2 = str(int2)

# ============================================
# 3、TODO str 与 tuple 之间的转换：

s = "www.baidu.com"
tp1 = s.split(".")  # ['www', 'baidu', 'com']
tp2 = tuple(tp1)    # ('www', 'baidu', 'com')

s1 = "www.baidu.com"
# 注意这种方式，直接转化的是将str中的每一个字符串都进行转化；
tp3 = tuple(s1)   # ('w', 'w', 'w', '.', 'b', 'a', 'i', 'd', 'u', '.', 'c', 'o', 'm')

# 元祖转换成 字符串;要采用遍历集合的形式
tp = ("we", "3", "fsd", "b")  # ==>"we.3.fsd.b"
a = ''
for n in tp:
    if n == tp[-1]:
        a = a + n
    else:
        a = a + n + '.'
print(a)    # 'we.3.fsd.b'

# ============================================
# 4、TODO str 与 float 之间的转换：

# 字符串 和 浮点型之间的转换是可以直接强制转换的；
str1 = "4521.32"
f1 = float(str1)   # 4521.32

f2 = 123.15
str2 = str(f2)
a = "".join(f2)

# ================================================
# 5、TODO str 与 dict之间的转换：
# 他们之间的转换只能讲keys 和values 分开转换的
import json
dict1 = {'name': 'Zara', 'age': 7, 'class': 'First'}
str1 = str(dict1.keys())
str2 = str(dict1.values())

# 字符串里字典转化 成字典，方式比较多；只列了两种
user_info = '{"name" : "john", "gender" : "male", "age": 28}'
user_dict = json.loads(user_info)
user_dict2 = eval(user_info)

import string
a = [13131]

b = ""
for i in a:
    if i == a[-1]:
        b = i

c = str(b)

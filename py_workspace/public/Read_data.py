# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/2 14:32
# @File 	:Read_data.py
# @Software :PyCharm


def read_text(path):
    data = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            l1 = line.replace("\n", "")
            l2 = l1.split("-")
            data.append(l2)

    return data

a= read_text("D:\java\Python\py_workspace\data\Register.txt")


def read_csv(path):
    data = []
    with open(path) as ff:
        for line in ff:
            data.append(line)
    return data







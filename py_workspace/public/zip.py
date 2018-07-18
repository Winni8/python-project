# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 14:08
# @File 	:zip.py
# @Software :PyCharm

import zipfile
import glob
import os

# file = "D:\\java\\Python\\py_workspace\\apk\\app-roseWholesale-develop0621.apk"  # 压缩apk是OK的
# file = r"D:\\java\\Python\\py_workspace\\report\\test_2018_06_28_11_08_20_545.html"  # 压缩单个文件OK
# 若果想压缩整个文件夹的话，就必须采用glob库，进行遍历集合；思路就是将整个文件夹使用glob库，转变成一个list，然后遍历


# TODO 压缩文件zip
def zipbag(file_path, after_path):
    files = glob.glob(file_path)            # 文件夹的路径
    print(type(files))                      # <class 'list'>
    zip_path = after_path                    # 指定压缩之后的路径
    f = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)

    # 遍历集合中的每一个文件
    for file in files:
        f.write(file)
    f.close()


# 调试作用，测试OK，出不来的时候，目录结构刷新一下
# file_path = "D:\\java\\Python\\py_workspace\\report\\*"  # 文件夹的路径
# after_path = "D:\\java\\Python\\py_workspace\\apk\\test.zip"  # 指定压缩之后的路径
# zipbag(file_path, after_path)

# TODO 解压文件unzip
def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_The bag after unzip"):
        pass
    else:
        os.mkdir(file_name + "_The bag after unzip")
    for names in zip_file.namelist():
        zip_file.extract(names, file_name + "_The bag after unzip/")
    zip_file.close()


# 调试作用 ，测试OK
# zip_path = "要unzip的zip包路径"   # 要unzip的zip包路径
# un_zip(zip_path)

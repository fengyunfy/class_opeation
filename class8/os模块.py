import os
#获取当前文件的目录
now_path = os.getcwd()
print(now_path)
#获取上一级目录
before_path = os.path.dirname("D:\PyCharm_Project\class8\os模块.py")
print(before_path)
#获取绝对路径
abs_path = os.path.abspath()
print(abs_path)

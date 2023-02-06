import os
print("获取当前模块路径",os.getcwd())
path = os.getcwd()
#获取当前项目的路径  os.getcwd()
print("获取当前项目的路径：",path)
#获取上一级路径   os.path.dirname(path)
dirname = os.path.dirname(path)
print("目录路径：",dirname)
#路径的拼接   --->os.path.join(path1,path2)
path1 = os.path.join(path,"A")
print(path1)
#class08下创建文件夹A
# os.mkdir(path1)
#把当前路径进行分解--->把路径拆分成路径+文件
file_path = "D:\PyCharm_Project\class8\os模块的应用.py"
split1 = os.path.split(path1)
new = os.path.split(file_path)
print(split1,new)

# 获取文件的访问权限
value = os.access(path1,os.F_OK)
print(value)
value1 = os.access(path1,os.R_OK)
print(value1)
#更改目录权限
import stat
os.chmod(path1,stat.S_IROTH)
"""
os模块---》对于文件目录进行操作  实现对于文件的操作与管理
1.创建修改删除重命名文件/目录
2.获取文件目录lujing
3.获取文件目录属性
4，修改查询文件权限
"""




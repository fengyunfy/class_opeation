import os
file_path = os.getcwd()
print("当前文件路径:",file_path)
#当前路径下创建文件夹aaa
if os.path.exists("aaa") == True:
    pass
else:
    AAA_path = os.path.join(file_path,"aaa")
    os.mkdir(AAA_path)
'''
获取文件的上一级路径
'''
before_path = os.path.dirname(file_path)
print('目录路径',before_path)
#分解文件路径
new_path = os.path.split(before_path)
print(new_path)

#获取当前的文件的绝对路径
abs_path = os.path.abspath("A")
print(abs_path)

real_path = os.path.dirname( os.path.abspath("A"))
print(real_path)

#返回当前文件的文件名
print(os.path.basename(file_path))

#分割文件夹路径
path_info = os.path.split(file_path)
print(path_info)

#获取文件的访问权限
os.access()
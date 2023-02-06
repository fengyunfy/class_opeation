import shutil

strl1 = """
# 1234567890abcdefg
# python全栈自动化测试
# 接口自动化
# web自动化
# """
# file = open("20210411.txt","w+",encoding="utf-8")
# #业务代码 可能也会异常，后面代码不会执行，file.close()不会执行
# file.writelines(strl1)
# file.close()
#
# with open("20210419.txt","w+",encoding="utf-8") as file:
    #文件一旦有任何异常会自动关闭文件流
    # file.writelines(strl1)#写入多行内容
#
# #读取文件中的内容
# with open("20210411.txt","r",encoding="utf-8") as file2:
#     # print(file2.read(10))
#     # print(file2.readline())
#     # print(file2.tell()) #指针位置
#     # # print(file2.readline())
#     print(file2.tell())
#     file2.seek(2,0)#改变指针位置
#     print(file2.tell())
#     print(file2.readline())
# # file2.encoding
# # file2.name
# # file2.


#
# file = open("123.txt","w+",encoding="utf_8")
# file.writelines("222")
# file.close()
# file = open("123.txt","a+",encoding="utf-8")
# file.writelines('123')
# file.close()
# file = open("123.txt","r+",encoding="utf-8")
# file.writelines("000")
# file.close()
#

# with open("232323.txt","r") as f:
#     f.read()

f = open('11028.txt','w+')
f.write("dsdsadsadsd"+"\n2323123213123"+"\newqeweqwewqewqewqe")
f.close()

# with open("1028.txt","r") as f :
#     f1 = f.read()
#     print(f1)
#     f.close()

with open("11028.txt",'a') as f :
    f1 = f.writelines("\n123213213123213"+"\nmmmxmxnmcnvmnbv")
    f.close()

f = open('11028.txt','r')
f1 = f.readline()
f2 = f.readline()
print(f1,f2)
f.close()
import os
if os.path.exists("1028.txt"):
    os.remove('1028.txt')
else:
    print("the file dose not exist")

with open('11028.txt','a') as f1:
    f1.seek(0,1)
    f1.write("2222")
with open("11028.txt",'r') as f2:
    f3 = f2.read()
    print(f2.tell())
    print(f3)

import os

now_path = os.getcwd()
print(now_path)
all_pathfile = os.listdir(now_path)
new_file = 'qwew'
if all_pathfile.count(new_file) == 0 :
    os.mkdir('D:\PyCharm_Project\内置函数\qwew')
else:
    print("该文件已存在")
# os.rmdir('D:\PyCharm_Project\内置函数\qwew
with open("qwew\\2222.txt",'w')as f:
    f.write('你好')

with open(r"qwew\ewew.txt","w") as f:
    f.write('dhsadsjjksadhkjasd')
# shutil.rmtree("D:\PyCharm_Project\内置函数\qwew")

os.rename("qwew",'weew')

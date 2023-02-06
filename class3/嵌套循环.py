#嵌套循环
"""
for里嵌套while，while里面嵌套for，for里面嵌套for,while里面嵌套while
"""
# *
# **
# ***
# ****
# *****
#非嵌套
for i in range(1,6):
    print("*"* i)#循环体里面-->重放做某件事情1* 2**...---》n n*
print("打印完成")
#嵌套
for i in range(1,7):
    #循环体里面-->重放做某件事情1* 2**...---》n n*
    for x in range(1,i):
        print("*",end="")
    print()
print("打印完成")
#9*9乘法表


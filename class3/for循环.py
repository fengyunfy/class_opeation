"""
for 变量 in 序列：
    执行语句1
else：
    执行语句2

运行逻辑，遍历序列（元素，列表，字典，字符串）中所有元素，每次遍历都会执行语句1
之后执行语句2
序列长度决定次数
"""
num = 0
list= []
sum= 0
while num < 100:
    num += 1
    list.append(num)
else:
    print("ok")
for i in list:
    sum +=i
else:
    print("运行结果是：",sum)
#range(n,m)  返回的n,m整数列表，含头不含尾返回列表中包含n,不包含m
sum1 = 0
for a in range(101):
    sum1 +=a
print(sum1)


#跳出整个循环体 break
#跳出本次循环continue
#pass空语句：确保程序结构的完整性
for i in range(1,11):
    if i <= 5:
        continue
    print(i)


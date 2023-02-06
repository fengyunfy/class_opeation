#定义元组，元组可以创建多个数据
tup1 = (1,2,"问问3")
print(type(tup1))
#创建空元组
tup2 = ()
print(tup2)
print(type(tup2))
#创建只有一个元素的元组,后面需要添加逗号（,）
tup3 = (1,)
print(type(tup3))
#获取元组中某个数据的值或多个数据的值--->切片
tup3 = tup1[0]
print(tup3)
print(tup1[0],tup1[1])
print(tup1[::-1])
#tuple中数据不可修改
new_tup = tup1 + tup1
print(new_tup)
#删除元组
del new_tup
#元组运算符 + * 重复 in存在 not in不存在
new_tup = tup1 *3
print(new_tup)
tup4 = (1,2,3,4,5,6)
if 1 in tup4:
    print("存在")
else:
    print("不存在")
strl ="1"
print(strl*10)
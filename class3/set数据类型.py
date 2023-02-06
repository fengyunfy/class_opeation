"""
集合set类型:表示符{}--->和字典{}相同表示怎么区分
可以存储多个元素,只支持不可变数据类型(string,number,tuple)
注意:
1.如何区分集合{} --->字典的表示形式是不一样的
2.元素类型:只支持不可变数据类型(string,number,tuple)
"""
set1 = {1,2,3,4,5,6,(12,23,123)}
print(set1)
print(type(set1))
#创建一个空集合
null = set()
print(type(null))
#获取集合某个元素或者多个元素???
#运算
#交集 A&B 取两个集合的相同元素
A={1,2,3,4,5}
B={2,3,5,6,7,8}
new = A&B
print(new)
print("交集",A.intersection(B))
#并集  合并A和B集合,返回的集合,既会包含A集合所有元素也会包含B集合所有元素
new1 = A|B
print(new1)
print("并集",A.union(B))
#差集 A-B 返回A集合的所有元素但是不会包含B集合中的元素
new2 = A-B
print(new2)
print("差集",A.difference(B))
#异或 A^B 返回的两个集合相同元素之外的其他元素的集合
new3 = A^B
print(new3)
print("异或",A.symmetric_difference(B))
#子集
son = {3,5}
print(son.issubset(A))

tup = (1,23,4,34)
tup1 = list(tup)
print(tup1[0])

#isdisjoin(判断两个集合是否包含相同集合,如果有返回True)
# set.add()
# set.update()
# set.remove()

"""
比较关系运算符：==、!=、>、>=、<、<=
"""
#  = 代表赋值
#  ==判断
#  1==2
if 1 == 2 :
    print(对)
else:
    print("不对")


mima = input("请输入你的密码:")
print("我的密码",mima)

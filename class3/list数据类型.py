"""
string：‘’ “” “”“”“”
元组：（）
列表：通过[]也可以存储多个数据，数据类型可以不一样，并且可以支持多种类型，元素与元素之间也是通过逗号（,）隔开
"""

list1 = [1,1.23,(1,2,3),"hello",[123]]
print(type(list1))
#获取list中最后一个数据，位置元素，部分元素---》切片  变量名[开始索引:结束索引:步长]
list2=list1[-1]
print(list2)
list3 = list1[0:4]
print(list3)

# list属于可变数据类型
del list1[0]
print(list1)
# list可以支持运算 + - * / in not in
list1 = list1 +['123',123,"wowo"]
print(list1)
print(list1 *2)

"""
list中常见的内置函数
操作:添加/删除/查找 元素
"""
#操作:添加元素append()
list_insert = [1,2,3,4,5]
list_insert.append(6)  #append做增加操作,append()返回的是空
print(list_insert)
#增加0,最前面   insert(index,object)指定位置插入
list2.insert(0,222)
print(list2)
#需要批量添加多个值到列表中 6,7,8,9,10,通过extend添加至list内
list2.extend([1,333,232323,"dsdasasd"])
print(list2)
#删除1  pop()
list4 = [1,"dididi",'大地',(12.2,23,"浪费")]
print(list4)
list4.pop()  #不传入索引值,则删除最后一个,否则删除指定索引值的元素,pop()会返回删除的值
print(list4)
list5 = [23,"ddd",'阿达哒哒哒',(23.2,15,"问")]
del_vlaue = list5.pop()
print(del_vlaue)
print(list5)
#删除2 clear()清空列表数据
list5.clear()
#删除3 remove()
list5.append(123)
list5.insert(0,121212121212)
list5.extend([1,2,3,4,5,6,7,8,9])
print(list5)
# remove与pop区别? remove--根据值进行删除  pop--根据索引进行删除
list5.pop(2)
print(list5)
list5.remove(9)
print(list5)

#复制
list6 = list5.copy()
print(list6)

#查找
print(list6.index(123))  #查到到返回值的索引值,否则抛出异常

#查找某个元素在列表中出现的次数
print(list6.count(123))

#列表进行排序
list6.sort()
print(list6)
#列表反转
list6.reverse()
print(list6)




"""
dict字典数据类型: 可以存储多个元素,元素表示形式键值对方式key:value
元素与元素之间通过逗号(,)隔开
表示符   {key:value,key:value}
dict数据类型是可变的
注意:1.key不可以重复,否则取最后的值      key的唯一性,我们可以通过key来取值
    2.key必须是不可变数据类型(string,tuple,number)
"""
info = {"name":"din","class":"M211期"}
#字典中某个元素的值  --->字典不能通过索引位置值来取值 取值:变量名[key]
print(info["name"])
print(info.get("name"))
#修改元素的值
info["class"] = "m212"
print(info)
info["address"] = "shengzheng"
info1 = info.copy()
print(info1)
#删除元素
del info["name"]
print(info)
info1.clear()
print(info1)

#创建一个字典,key确定,值不太确定,设置value-->默认值null
keys = ["name","address"]
info2 = dict.fromkeys(keys,"null")
print(info2)
#需要循环的读取到字典中的所有数据key,value
print(info1)
print(info)
for x,y in info.items():  #item --->返回一个序列,包含key和value的值
    print(x,y)
#字典的合并 --->更新字典
add = {"sale":"15000","qwxz":"25000"}
info.update(add)
print(info)
#删除某个元素
print(info)
info.pop("address") #根据key进行删除
info.popitem() #默认删除最后一个元素,否则报异常


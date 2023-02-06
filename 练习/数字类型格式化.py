"字符串进行格式化"
#一、占位符
print("姓名：%s,工作年限：%s，性别：%s"%("limi","12","男"))

#format函数
print("姓名：{},工作年限:{},性别:{}".format("limi","12","男"))

#f 字面量格式化
name = "limi"
year = 12
sex = "男"
print(f"姓名：{name},工作年限:{year},性别:{sex}")

join_str ="hello world!"
new_str = "-".join(join_str)
print(new_str)


spilt_str = "123;we;23;23;566767;;rr; ;t"
new_str_list = spilt_str.split(";")
print(new_str_list)

name = "123"
print(id(name))
print(id(name+"112"))

replace_str = "123123123"
new_str1 = replace_str.replace("123123123","123")
print(new_str1)


find_str = "hello world!"
find_index = find_str.find('f')
print(find_index)
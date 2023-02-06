#1.计算天数
days = 0
run_year = 0
ping_year = 0
# 1900-2022年，闰年的个数，平年的个数
for i  in range(1900,2022):
    # print(i)
    #判断闰年的规则：能被4整除，不能被100整除，或者能被400整除

    if (i % 4 == 0 and i %100 !=0) or i % 400 == 0:
        # print("闰年")
        run_year += 1
        # print(run_year)
        days += 366
    else:
        # print("平年")
        ping_year += 1
        days+=365

# days = run_year*366 +ping_year*365
print(days)
# 2022年1月1日至今的天数，求每个月的天数
for month in range(1,9):
    if month in [1,3,5,7,8,10,12]:
        days+=31

    elif month == 2:
        i = 2022
        if (i % 4 == 0 and i %100 !=0) or i % 400 == 0:
            days+=29
        else:
            days+=28
    else:
        days+=30
print(days)
days = days+17
print(days)
# 2.
strl = input("请输入：")
strl1 = "-".join(strl)
strl2 = strl1.split("-")
print(strl2)
a = 0
for i in strl2:
    if i  ==  " ":
        a +=1
    else:
        pass
if a > 0 :
    print("True")
else:
    print("False")
# 什么时候需要返回值，什么时候不需要返回值 ，需要获取函数体中的值时，后面的方法需要这个函数
def is_nullstr(zf):
    for i in zf:
        if i ==" ":
            return True
    return False
zf = "hello world!"

value = is_nullstr(zf)
print(value)




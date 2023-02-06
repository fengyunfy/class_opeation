# 1.计算1900年1月1日到今天相距多少天
"""遍历所有到今年前的所有年份
1.闰年能被4整除无法被100整除
2.其他的都是平年
"""
run_year = 0
ping_year = 0
days = 0
for year in range(1990,2023):
    if year % 4 == 0 and year % 100 > 0:
        run_year += 1
        days += 366
    else:
        ping_year += 1
        days += 365
    print(year)
print(run_year,ping_year)
now_year = 2023
month = input("输入所在月份")
for now_month in range(1,int(month)):
    if month  in [1,3,5,7,8,10,12]:
        days += 31
    elif month == 2:
        if now_year % 4 == 0 and now_year % 100 > 0:
            days += 28
        else:
            days += 29

    else:
        days += 30
days = days+16
print(days)



#单一条件:大于60及格,小于60不及格-->条件控制语句
score = int(input("请输入你的成绩:"))
if score >= 60:
    print("及格")
else:
    print("不及格")

# 条件一为真,执行代码块1
# 条件一为假,执行代码块2

#多个条件:多重if
"""
if 条件一:
    代码块1
else 条件二:
    代码2
else 条件三:
    代码3
    ...
else:
    代码...
"""
score1 = int(input("请输入你的成绩:"))
if score1 > 60:
    # print("不及格")
    if score1>60 and score1<70:
        print("合格")
    elif score1>=70:
        print("优秀")
else:
    print("不合格")

if score1 < 60:
    print("不及格")
elif score1>60 and score1<70:
    print("合格")
elif score1>=70:
    print("优秀")

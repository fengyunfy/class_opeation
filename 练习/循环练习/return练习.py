# a = input("输入：")
# a1 = ";".join(a)
# a2 = a1.split(";")
# print(a2)
# if a2.count(' ')>0:
#     print("True")
# else:
#     print("False")


def isNullStr(zf):
    for s in zf:
        if s ==" ":
            return True
    return False


zf ="123213123123"
value = isNullStr(zf)
print(value)
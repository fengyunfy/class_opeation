#必须参数
def info(name,age):
    print(f"姓名:{name},年龄:{age}")

#调用函数
name = "dong"
age = "18"
info(name,age)


def info1(name,age,classname):
    print(f"姓名:{name},年龄:{age},班级:{classname}")

classname = "M211"
info1(name,age,classname)  #按照定义顺序定义参数个数
#关键字参数  不按顺序传参
#允许函数调用参数顺序与声明不一致
info1(age=12,name=12,classname=12)

#默认参数  定义与调用函数  定义函数时继续默认值赋值

def info2(name,age,classname="M211"):
    print(f"姓名:{name},年龄:{age},班级:{classname}")
#设置默认值参数 是否可以通过关键字参数进行调用或者必须参数进行调用   是可以的
#默认参数函数   默认参数可以不赋值   则取默认值
info2(name,age)
#默认参数能否赋值  可以   调用参数：必须参数，关键值参数

#不定长参数：你可能需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数
#实现求几个数的和  几个数不确定？
#形式一    *参数  --》把多个参数基于元组方式进行存储
#**参数基于字典的方式进行存储
#*号单独出现的时候， 后面的参数必须通过关键字传参


def sum(a,b):
    return a + b
#求和
def sum1(*num):
    print(num)       #元素是每个参数的值
    print(type(num)) #元组
    print(num[-1])
    a = 0
    for x in num:
        a += x
    print(a)
    return a
        # while x == num[-1]:
        #     print(a)
        #     break


    pass #占位语句，暂时没想好，空语句

sum1(1,2,3,4,5,6)


def sum2(**num):
    print(type(num))


sum2(num=1,num2 = 2,num3 =3)

def sum3(num1,num2,*,num3):
    return num1+num2+num3
print(sum3(1,2,num3=3))

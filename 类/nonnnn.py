class jj():
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "放置得家具是%s，占地面积为%d"%(self.name,self.area)


bad = jj("床",4)
print(bad.__str__())


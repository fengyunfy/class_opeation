class fangzi():

    def __init__(self,jj_name,jj_mj):
        self.jj_name = jj_name
        self.jj_mj = jj_mj
        self.jj_list = []
        self.zmj =100


        self.fz = [self.zmj,self.symj,self.jj_list]


    def jj_add(self):
        self.jj_list.append(self.jj_name)
        self.symj = self.zmj -self.jj_mj
        self.fz[2] = self.symj
        print(self.fz)

chuang = fangzi("床",4)
chuang.jj_add()
yigui = fangzi("衣柜",2)
yigui.jj_add()
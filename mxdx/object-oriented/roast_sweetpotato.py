class RostPotato():
    def __init__(self):
        self.cookedlevel=0
        self.cookedstring='生的'
        self.cookediments=[]

    def __str__(self):
        msg=self.cookedstring+'地瓜'
        if len(self.cookediments)>0:
            for i in self.cookediments:
                msg=msg+i
        return msg
    def cook(self,time):
        self.cookedlevel=time
        if self.cookedlevel<=3:
            self.cookedstring='生的'
        elif self.cookedlevel<=5:
            self.cookedstring='半生不熟'
        elif self.cookedlevel<=8:
            self.cookedstring='熟了'
        else:
            self.cookedstring='木炭状'
    def addcondiments(self,codiments):
        self.cookediments.append(codiments)
rp=RostPotato()
rp.cook(5)
rp.addcondiments('番茄酱')
rp.addcondiments('豆瓣酱')
print(rp)

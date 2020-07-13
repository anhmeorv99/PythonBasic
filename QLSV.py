
class QLSV:
    def __init__(self,mssv,hoten,cpa):
        self.mssv=mssv
        self.hoten=hoten
        self.cpa = cpa
    

    def getName(self):
        return self.hoten
    def getMSSV(self):
        return self.mssv
    def getCPA(self):
        return self.cpa

    def setName(self,name):
        self.name = name
    def setMSSV(self,mssv):
        self.mssv = mssv
    def setCPA(self,cpa):
        self.cpa=cpa

    def showSV(self):
        print(self.mssv,'\t',self.hoten,'\t', self.cpa,'\n')
    def nhapSV(self):
        self.mssv = str(input('Nhap MSSV :'))
        self.hoten = str(input('Nhap Ho Ten SV:'))

    

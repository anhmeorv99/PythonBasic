from QLSV import QLSV
class Main():

    A = []
    for i in range(0,2):
        SV = QLSV()
        SV.nhapSV()
        A.append(SV)
    for x in A:
        x.showSV()

    
        
    
        
    
    



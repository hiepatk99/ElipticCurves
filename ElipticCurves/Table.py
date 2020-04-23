from SumPoint import *

#lập bảng toạ độ từ phần tử sinh của đường cong
def PrimitiveElementTable(a,b,p,p1):
    PETable = [p1]
    while 1:
        newPoint = Point(PETable[0],PETable[-1],p,a)
        PETable.append(newPoint)
        if(PETable[0][1]==PETable[-1][1]):
            break
#    z = 1
#    print('k\tlamda\tx\ty')
#    for i,j,k in PETable:
#        print(z,'\t',i,'\t',j,'\t',k)
#        z+=1
#    del i,j,k,z
    return PETable
#PrimitiveElementTable(-1,188,751,(0,0,376))

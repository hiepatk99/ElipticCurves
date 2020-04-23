from SumPoint import *
from Table import *
a = input("A=")
b = input("B=")
p = input("P=")
A, B, P = int(a), int(b), int(p)
del a,b,p
#y^2 = x^3 + Ax + B 
# điều kiện: (4A^3 + 27B^2) mod p != 0
#Tính Qp
if((4*A**3 + 27*B**2)%P!=0):
    i = 1
    Qp = [] #phần tử nguyên thuỷ
    while(i <= P/2):
        q = i**2%P
        Qp.append(q)
        i+=1
    del i
    Ep = [] #toạ độ đường cong elipstic
    for i in range(0,P):
        q_ = (i**3 + A*i + B)%P
        if q_ in Qp:
            Ep.append((i,Qp.index(q_)+1))
            Ep.append((i,P - Qp.index(q_) - 1))
    del i,q_
    PETable = []
    for i in Ep:
        p1 = (0,) + i
        CoordinatesTable = PrimitiveElementTable(A,B,P,p1)
        if(len(CoordinatesTable)!=len(Ep)):
            CoordinatesTable.clear()
        else:
            PETable = CoordinatesTable.copy()
            break
    del i,p1,CoordinatesTable
    print('Select 1: show Ep.\nSelect 2: show PETable')
    select = input('Chose:')

    print(select)
    if select=='1':
        print("Danh sách điểm thuộc đường cong Ep(a,b)")
        print('x\ty')
        k = 1
        for i,j in Ep:
            print(k,'\t',i,'\t',j)
            k+=1
        del i,j,k
    elif select == '2':
        print("Bảng kG (với G là phần tử sinh đầu tiên tìm được)")
        z = 1
        print('k\tlamda\tx\ty')
        for i,j,k in PETable:
            print(z,'\t',i,'\t',j,'\t',k)
            z+=1
        del i,j,k,z
    print('Bậc của Ep là: ',len(Ep)+1)
    input("Press any key to close program")

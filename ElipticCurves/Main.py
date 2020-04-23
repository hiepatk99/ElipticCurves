from SumPoint import *
from Table import *
from Eratos import *
a = input("A=")
b = input("B=")
p = input("P=")
A, B, P = int(a), int(b), int(p)
del a,b,p
#y^2 = x^3 + Ax + B 
# điều kiện: (4A^3 + 27B^2) mod p != 0

if((4*A**3 + 27*B**2)%P!=0):

    #Tính Qp
    i = 1
    Qp = [] #phần tử nguyên thuỷ
    while(i <= P/2):
        q = i**2%P
        Qp.append(q)
        i+=1
    del i

    #Tìm các điểm thuộc đường cong
    Ep = [] #toạ độ đường cong elipstic
    for i in range(0,P):
        q_ = (i**3 + A*i + B)%P
        if q_ in Qp:
            Ep.append((i,Qp.index(q_)+1))
            Ep.append((i,P - Qp.index(q_) - 1))
    del i,q_
    print('Bậc của Ep là: ',len(Ep)+1)

    #Bảng kP với P là phần tử sinh đầu tiên tìm được
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

    print('Select 1: hiển thị danh sách điểm thuộc Ep.')
    print('Select 2: hiển thị danh sách kG với G là 1 điểm thuộc Ep')
    print('Select 3: hiển thị danh sách phần tử sinh')
    select = input('Chose:')

    if select=='1':
        print("Danh sách điểm thuộc đường cong Ep(a,b)")
        print('x\ty')
        k = 1
        for i,j in Ep:
            print(k,'\t',i,'\t',j)
            k+=1
        del i,j,k

    elif select == '2':
        print('Nhập toạ độ điểm G(x,y)')
        x = input('x=')
        y = input('y=')
        G = (0,int(x),int(y))
        del x,y
        PETableG = PrimitiveElementTable(A,B,P,G)
        z = 1
        print('k\tlamda\tx\ty')
        for i,j,k in PETableG:
            print(z,'\t',i,'\t',j,'\t',k)
            z+=1
        del i,j,k,z
        print('Bậc của G là ',len(PETableG)+1)

    elif select == '3':
        prime = EratosTable(len(Ep) + 1)
        for i in PETable:
            z = PETable.index(i)
            if prime.count(z) != 0 or z == 0 or z == 1:
                print(i) 
    input("Press any key to close program")

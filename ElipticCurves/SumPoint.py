def SwitchModunlo(a, b):
    #Tính b^-1 mod a
    x1, x2, y1, y2 = 0, 1, 1, 0
    r = q = x = y = 0
    while(b!=0):
        q = int(a/b)
        r = a%b
        x = x2 - x1*q
        y = y2 - y1*q
        x2, y2 = x1, y1
        x1, y1 = x, y
        a = b
        b = r
    return y2

#Tính lamda của 2 điểm
def Lamda(tupP1, tupP2, p, a):
    #tupP1 gồm (lamda, x1, y1)
    #tupP2 gồm (lamda, x2, y2)
    x1, y1 = tupP1[1], tupP1[2]
    x2, y2 = tupP2[1], tupP2[2]
    if tupP1 == tupP2:
        TL = (3*x1**2 + a)%p
        ML = (2*y2)%p
    else:
        TL = (y2 - y1)%p
        ML = (x2 - x1)%p
    ML = SwitchModunlo(p,ML)
    lamda = (TL*ML)%p
    return lamda

def Point(tupP1, tupP2, p, a):
    #tupP1 gồm (lamda, x1, y1)
    #tupP2 gồm (lamda, x2, y2)
    lamda = Lamda(tupP1, tupP2, p, a)
    x1, y1 = tupP1[1], tupP1[2]
    x2, y2 = tupP2[1], tupP2[2]
    x3 = (lamda**2 - x1 - x2)%p
    y3 = (lamda*(x1 - x3) - y1)%p
    tupP3 = (lamda, x3, y3)
    return tupP3

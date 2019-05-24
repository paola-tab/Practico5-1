def max2(a,b):
    a=input("ingrese primera variable")
    b=input("ingrese segunda variable")
    if a > b:
        print (a,"es mayor que ",b)
    elif b > a:
        print (b,"es mayor que ",a)
    else:
        print (a, "y" ,b, "son iguales")
    return

def max3(c,d,e):
    c=input("ingrese primera variable")
    d=input("ingrese segunda variable")
    e=input("ingrese tercer variable")
    if c > d and c > e and d != e:
        print (c,"es mayor que ",d, "y" ,e)
    if d > c and d > e and c != e:
        print (d,"es mayor que ",c, "y" ,e)
    elif e > c and e > d and c != d:
        print  (e, "es mayor que " ,c, "y" ,d)
    else: 
        print ("ERROR! LOS NUMEROS DEBEN SER DISTINTOS")
    return

def lista(cantidad):
    cantidad=input("ingresa lista")
    total=0
    for x in cantidad:
        total += 1
    print (total)
    return

def vocal_o_consonante (v):
    v=input("ingresa Letra")
    if v== 'a' or v=='e' or v=='i' or v=='o' or v== 'u':
        print (v,"Es vocal")
    else:
        print (v,"Es consonante")
    return 

def sumalista(lis):
    lis=input("ingrese lista")
    laSuma = 0
    for i in lis:
        laSuma = laSuma + i
    return laSuma


def produlista(prod):
    prod=input("ingrese lista ")
    mul = 1
    for i in prod:
        mul = mul * i
    return mul




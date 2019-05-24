def Comparalista(a,b):
    a=input('Ingresa Primera Lista ')
    b=input('ingresa Segunda Lista ')
    comparacion= [item for item in a if item in b]
    if len (comparacion) > 0:
        print 'Ambas Listas Contienen Estos Elementos'
        for item in comparacion:
            print '%s' % item
    else:
        print 'No Existe Ningun Elemento Comun Entre Las Listas'

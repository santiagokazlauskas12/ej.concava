"Ver si una lista de numeros es concava "


lista=[3, 2, 1, 0, 1,2,3,4,5,6,7,8]


def esConcava(lista):

    caunt=1
    count=0
    x=None
    y=None

    for lessnumber in lista :
        if x == None:
            x=lessnumber
        elif lessnumber < x:
            x=lessnumber
            count=count+1

    for greatnumber in lista[count: ]:
        if y==None:
            y=greatnumber
        if greatnumber > y:
            y=greatnumber
            caunt=caunt+1

    if len(lista)== caunt+count:
        return True
    else:
        return False

print(esConcava(lista))

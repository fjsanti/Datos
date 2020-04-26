''''
Este pequeño scrip crea una funcion para contar cuantas veces se
repite un dato en una lista que se da como la entrada de la funcion. 
Por ejemplo:
frequencyTable([a, a, b, b, c])

Retorna:
ITEM FREQUENCY
a    2
b    2
c    1

''''

def frequencyTable(alist):

    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1
    itemlist = list(countdict.keys())
    itemlist.sort()

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item, "   ", countdict[item])

    return None

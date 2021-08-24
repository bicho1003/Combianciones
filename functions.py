listcom = []
def combinaciones(numcom):
    i = 0
    numlv = 0
    while i < numcom:
        j = 0
        listcom.append([])
        numlv = int(input("Cuantos RESULTADOS tiene en su experimento simple %d :" %(i+1)))
        while j < numlv:
            listcom[i].append(input("Por favor introdusca el resultado %d: " %(j+1)))
            j = j + 1
        i = i + 1
    for i in listcom:
        print (i)
    
    return listcom


def mostrar(listcomb):
    listRes = []
    i=0
    j=0
    totalcomb = 1
    totalcomb2 = 0
    print("A continuacion le voa mostrar las posibles combinaciones\njunto con el total de combinaciones que se pueden obtener dentro de su experimento")


    for x in listcomb:
        totalcomb = totalcomb*len(listcomb[j])
        j=j+1
        print(totalcomb)
    
    totalcomb2 = totalcomb

    while totalcomb2>0:
        listRes.append([])
        totalcomb2 = totalcomb2 - 1
    

    for i in listRes:
        print(i)

mostrar([["Zapato","Zapatilla"],["Camisa","Vestido"]])
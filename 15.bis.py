#Funció sumar elements de la llista
def sumar_llista(a):
    sumatori=0
    for i in a:
        sumatori+=(i*i)
    return sumatori
#Funció multiplicar element de la llista
def multiplicar_llista(b):
    multiplicat=1
    for x in b:
        multiplicat*=x
    return multiplicat

#Programa principal
i=[1,3,4,5,7]
print("El sumatori és: ", sumar_llista(i))
print("La multiplicació dels elements de la llista és: ", multiplicar_llista(i))
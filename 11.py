# Definició de funcions
def Gran(x,y):
    a=x
    if(x>y):
        print(x, "es major...",y)
    elif(y>x):
        print(y,"es major...",x)
        a=y
    else:
        print(x,"és igual que",y)
    return a

# Aplicació principal
    a=int(input("Número 1"))
    b=int(input("Número 2"))
    c=gran(a,b)
    print("El més gran val:",c)
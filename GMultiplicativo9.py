xn = 19
a = 2
m = 16381
num = 0
contador = 0
vistos = set()
limite = 2**32
for i in range(2*m):
    num = (a * xn) % m
    #print (num / m)
    if(num in vistos):
        print(f" Se repitio el numero tras {contador} numeros")
        break
    vistos.add(num)
    contador += 1
    xn = num
if(contador == m-1):
    print ("Cuenta con periodo completo")
else:
    print("NO cuenta con periodo completo, periodo: ", contador)
print ("FIN")
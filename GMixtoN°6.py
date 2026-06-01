xn = 31
a = 20000001
m = 10**8
c = 11
num = 0
contador = 0
vistos = set()
limite = 1000000000
for i in range(limite):
    num = ((a * xn) + c) % m
    #print (num / m)
    if(num in vistos):
        print(f" Se repitio el numero tras {contador} numeros")
        break
    vistos.add(num)
    contador += 1
    xn = num
if(contador == m):
    print ("Cuenta con periodo completo")
else:
    print("NO cuenta con periodo completo, periodo: ", contador)
print ("FIN")
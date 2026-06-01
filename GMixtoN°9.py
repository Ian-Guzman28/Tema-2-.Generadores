xn = 11
a = 41
m = 20000
c = 3
num = 0
contador = 0
vistos = set()
limite = 2**32
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
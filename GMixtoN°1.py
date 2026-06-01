xn = 17
a = 200001
m = 10**6
c = 1
num = 0
contador = 0
vistos = set()
limite = 10000000
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
from functools import reduce
lista = [2,4,6,8,10,12,14,16,18,20]

#función con expresión lambda
cuadrado = lambda x: x**2
print(cuadrado(3))

#uso de currificación
def incrementador(n): return lambda x: x + n
f = incrementador(2)
g = incrementador(3)

print(f(25))
print(g(25))

#aplicación de map
c = [39.2, 36.5, 37.3, 38, 37.8] 
f = list(map(lambda x: (float(9)/5)*x + 32, c))
print(f)
c = list(map(lambda x: (float(5)/9)*(x-32), f))
print(c)

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print(list(map(lambda x,y:x+y, a,b)))
print(list(map(lambda x,y,z:x+y+z, a,b,c)))
print(list(map(lambda x,y,z : 2.5*x + 2*y - z, a,b,c)))

mapeada = map(cuadrado, lista)
print(list(mapeada))


#aplicación de filtros

filtrada = filter(lambda x: x % 3 ==0, lista)
print(list(filtrada))

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

#aplicación de reduce
print(reduce(lambda x,y: x+y, lista))

f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))

print(reduce(lambda x, y: x*y, range(1,49)))



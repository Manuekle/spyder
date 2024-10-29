title = 'inteligencia artificial'

print('converitir mayusculas')
print(title.upper())

print('converitir minusculas')
print(title.lower())

print('converitir en mayuscula la primera letra')
print(title.capitalize())

#%%

title2 = 'int,eli,gen,cia'

print('eliminar una caracter')
print(title2.strip(','))
print(title2.split(','))

print('reemplazar una letra')
print(title2.replace('a','k').strip(','))

#%%

""" comparaciones """

a = 4
b = 8

print("f {a} > {b}", a > b)
print("f {a} < {b}", a < b)
print("f {a} >= {b}", a >= b)
print("f {a} <= {b}", a <= b)
print("f {a} == {b}", a == b)
print("f {a} >= {b}", a != 23)

#%%
import math

"""
realiza un programa donde el usuario ingrese 2 
numero enteros o flotantes y muestre las siguientes
operaciones comparacione
    distinto a 
    igual a 
    raiz cuadrada de 
    potenciacion de b
"""

a = float(input('ingrese un numero a = '))
b = float(input('ingrese un numero b = '))

print(a != b)
print(a == b)
raiz = math.sqrt(b)
print(raiz)
potencia = math.pow(b, 3)
print(potencia)

#%%

""" condicionales """

count = float(input('ingrese un numero: '))

if count > 0:
    print('numero positivo')
elif count < 0:
    print('numero negativo')
else:
    print('numero cero')

#%%

""" estructura iterativa for """

nums = [0,1,2,3,4,5,6,7,8,9]

# numeros pares
for i in nums:
    if i %2 == 0:
        print(i)
    
#%%
        
"""
solicita una lista de numeros separada por coma,
calcule el promedio de esos numero y imprima el promedio
"""        
        
list = '0,1,2,3,4,5,6,7,8,9'

a = list.split(',')
print(a)

l = len(a) 

for i in a:
    x += i
    print(x)

#%%

movies = ['toy story','chucky','alien']
singers = list(('metallica','deftones','slipknot'))
years =  list(range(2020,2050))
nums = [5,3,9,6,8,2,1,4]
mix = ['a',30,True,4.4]

print(type(movies))

# examples
movies[1] = 'black'
movies[-2] = 'mirror'

singers[2:4]

singers.append(('guns and roses'))
singers.insert(1, 'mm')
singers.pop(3)

nums.sort()
nums.reverse()

singers.remove('deftones')

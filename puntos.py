#%%
#1
num1 = 5
#/ = float(input('ingrese un numero a = '))
num2 = 9

def find_max(num1, num2):
    if num1 > num2:
        print("El mayor es:", num1)
    else:
        print("El mayor es:", num2)

find_max(num1, num2)

#%%
#2
num1 = 5
num2 = 7
num3 = 10

def find_max(num1, num2, num3):
    if num1 > num2 and num1> num3:
        print("El mayor es:", num1)
    elif num2 > num1 and num2 > num3:
            print("El mayor es:", num2)
    else:
        print("El mayor es:", num3)

find_max(num1, num2,num3)
#%%
#3
elemento =[1,2,3,4,5,6,7,8,9,10]
def calcular_longitud(elemento):
    contador = 0
    for _ in elemento:
        contador += 1
    return contador
calcular_longitud(elemento)    
#%%
#4
palabra = 'https'
def verificar_variable(palabra):
    if palabra[0] in ['a', 'e', 'i', 'o', 'u']:  
        print('TRUE')
    elif palabra[1] in ['a', 'e', 'i', 'o', 'u']:  
        print('TRUE')
    elif palabra[2] in ['a', 'e', 'i', 'o', 'u']:  
        print('TRUE')
    elif palabra[3] in ['a', 'e', 'i', 'o', 'u']:  
     print('TRUE')
    else:
     print('FALSE')
verificar_variable(palabra)  
#%%
#5
numeros = [1, 2, 3, 4]

def suma_numeros(numeros):
    return numeros[0] + numeros[1] + numeros[2] + numeros[3]

resultado = suma_numeros(numeros)
print(resultado)
#%%
#5
numeros = [1, 2, 3, 4]

def multiplicacion_numeros(numeros):
    return numeros[0] * numeros[1] * numeros[2] *numeros[3]

resultado = multiplicacion_numeros(numeros)
print(resultado)

#%% 
#6
def inversa(cadena):
    inversa = ""
    for i in range(len(cadena)-1, -1, -1):
        inversa += cadena[i]
    return inversa

cadena = "estoy probando"
cadena_invertida = inversa(cadena)
print(cadena_invertida)

#%% 
#7
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    inversa = ""
    for i in range(len(cadena)-1, -1, -1):
        inversa += cadena[i]
    return cadena == inversa

palabra = "radar"
es_palindromo = es_palindromo(palabra)
print(es_palindromo)


#%%
#8
def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

lista1 = [1, 2, 3]
lista2 = [4, 2, 6]
resultado = superposicion(lista1, lista2)
print(resultado)

#%%
#9
def generar_n_caracteres(n, caracter):
    resultado = ""
    for i in range(n):
        resultado += caracter
    return resultado

caracter = "x"
n = 5
resultado = generar_n_caracteres(n, caracter)
print(resultado)


#%%
#10
def procedimiento(lista):
    for numero in lista:
        print("*" * numero)
    

lista = [4, 9, 7]
procedimiento(lista)
print(procedimiento)
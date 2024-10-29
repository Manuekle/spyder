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
lista2 = [4, 9, 6]
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

    


#%%
#practica
a = 2 
b = 3
def suma (a,b):
   return a+b
resultado = suma(a, b)
print(resultado)
#%%
numero = 2
def par_o_impar (numero):
 if numero in [1,3,5,7,9]:
     print('False')
 else:
    print('True')
par_o_impar(numero)
#%%
def factorial_calcular (pedir):
    pedir = input('dame un numero:  ')
    resultado =  pedir*9/5+32
print(resultado)
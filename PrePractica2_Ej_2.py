#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

lista = []
lista_impar = []
x = 0

for x in range(5):
    numeros = int(input("Ingrese los valores de la lista: "))
    if numeros % 2 :
        lista_impar.append(numeros)
    else: 
        lista.append(numeros)
    
print("Lista completa: ") 
lista_completa = lista + lista_impar
print(lista_completa)

print("Lista par")
print(lista)

print("Lista impar ")
print(lista_impar)


 
#FIN
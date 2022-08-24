#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
a = input()
print ("ingrese un numero: ")
numero = input()
print ("ingrese otro numero: ")
numero_2 = input()
try:
        a = numero / numero_2
except ZeroDivisionError as exception:
        print (f"ha ocurrido un error | {exception}")
finally:
        print ("finalizado")
#FIN
#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = int(0)
elif edad >=4 and edad<=18:
    precio = int(5)
else:
    precio = int(10)

print("El precio a pagar es de $" + str(precio))
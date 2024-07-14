#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

numero1 = float(input("Ingrese un numero entero: "))
numero2 = float(input("Ingrese otro numero entero: "))

menu = print(f"""
             Escoja una opcion de las 3:
             1. Sumar los dos numeros
             2. Restar el primer numero menos el segundo
             3. Multiplicar los dos numeros
             """)

operacion = int(input("Seleccione una opcion de las 3: "))

if operacion == 1:
    resultado = (numero1 + numero2)
    print(resultado)
elif operacion == 2:
    resultado = (numero1 - numero2)
    print(resultado)
elif operacion == 3:
    resultado = (numero1 * numero2)
    print(resultado)
else:
    print("La opción escogida es inválida")


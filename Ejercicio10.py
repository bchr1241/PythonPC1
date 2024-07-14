#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']

lista_muestra = ["Rojo", "Verde", "Blanco", "Negro", "Rosa", "Amarillo"]
print("Esta es la lista inicial:")
print(lista_muestra)

del lista_muestra[5]
del lista_muestra[4]
del lista_muestra[0]

print("Esta es la lista con los elementos de las posiciones 0, 4 y 5 eliminados:")
print(lista_muestra)

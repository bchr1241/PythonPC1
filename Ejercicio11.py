#Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
#lista. Su programa debe retornar otra lista sin los duplicados.
#Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
#Lista procesada: [1, 2, 3, 4,, 5]

#Estableciendo la lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
print("Esta es la lista original:")
print(lista_original)

#Estableciendo la lista como conjunto y luego como lista de nuevo
lista_procesada = list(set(lista_original))
print("Esta es la lista sin duplicados:")
print(lista_procesada)
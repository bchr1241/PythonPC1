#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina.

consumo = float(input("Ingrese su consumo en el restaurante: "))
porcentaje = float(input("Ingrese el porcentaje de su consumo que le desea dejar en propina al mesero:"))
propina = consumo * (porcentaje/100)
print("Le estará dejando al mesero " + str(propina) + " dólares de propina")

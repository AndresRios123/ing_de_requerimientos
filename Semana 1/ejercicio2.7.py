# Conversión de galones a mililitros
galonesLitros = 3785

galonesLeche = int(input("Ingrese la cantidad de galones: "))

# Calculamos el equivalente en mililitros
litrosLeche = galonesLeche * galonesLitros

# Se imprime el resultado
print(f"El total de mililitros de leche es: {litrosLeche:,}")



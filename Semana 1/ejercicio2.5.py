# Cálculo del área de un triángulo
base = int(input("Introduce la base del triángulo: "))
altura = int(input("Introduce la altura del triángulo: "))
areaTriangulo = (base * altura) / 2
print(f"Área del triángulo: {areaTriangulo}")

# Cálculo del área de un rectángulo
baseRectangulo = int(input("Introduce la base del rectángulo: "))
alturaRectangulo = int(input("Introduce la altura del rectángulo: "))
areaRectangulo = baseRectangulo * alturaRectangulo
print("Área del rectángulo: " + str(areaRectangulo))

# Cálculo del area de la figura completa
areaCompleta = areaTriangulo + areaRectangulo
print("El área total combinada es: " + str(areaCompleta))
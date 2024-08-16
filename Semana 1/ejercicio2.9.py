# Pago semanal por trabajador
horasPorDia = int(input("Ingresa las horas trabajadas por día: "))
costoPorHora = int(input("Ingresa el costo por hora: "))

# Calculamos horas trabajadas en la semana (6 días)
horasSemanales = horasPorDia * 6

# Calculamos el costo semanal
costoSemanal = horasSemanales * costoPorHora

# Se muestra el pago semanal
print(f"El pago semanal es: {costoSemanal:,}")


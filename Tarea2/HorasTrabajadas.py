#0901-22-940-Edwin-Stevens-Cambranes-Mendizábal

#datos del trabajador
nomTrabajador = str(input("Bienvenido trabajador ingresa tu nombre: "))
horasTrabajadas = int(input("Ahora ingresa tus horas de trabajo por favor: "))
costeHora = float(input("Por ultimo ingresa el costo por hora trabajada: "))

pagaTrabajador = horasTrabajadas * costeHora #formula

print("Gracias por tus ", horasTrabajadas, " horas de trabajo ", nomTrabajador, " tu paga correspondiente sera de un monto total de: Q ", pagaTrabajador) #salida
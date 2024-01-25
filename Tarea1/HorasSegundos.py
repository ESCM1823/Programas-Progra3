# 0901-22-940-Edwin-Stevens-Cambranes-Mendizábal
# Un programa que calcule al ingresar la hora indique cuantos segundos han trascurido del dia.
hr = int(input("Ingrese la hora actual (con formato de 24 horas): "))
min = int(input("Ingrese los minutos actuales: "))

totalSegundos = (hr * 3600) + (min * 60)

print("Actualmente llevas: ", totalSegundos, " segundos trascuridos")

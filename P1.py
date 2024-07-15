#2
#defino el porcentaje de propina en eeuu como una constante
porcentaje_propina = 15
#solicito el monto de la cuenta
cuenta = float(input("Ingrese el total de la cuenta:  $"))
#Calcular la propina
propina = cuenta*(porcentaje_propina/100)
#Mostrar monto de la propina
print(f"El monto de la propina es: ${propina: .2f}")
#calcular el total con la propina
total_con_propina = cuenta + propina
#mostrar el total con propina
print(f"El total con propina es: ${total_con_propina: .2f}")


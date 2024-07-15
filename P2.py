#defino el peso de cada objeto
peso_payaso = 112 # gramos
peso_muñeca = 75 # gramos
#solicito cantidad de muñecas y payasos vendidos con int (valores enteros)
numero_payasos = int(input("cantidad de payasos vendidos: "))
numero_munecas = int(input("cantidad de muñecas vendidas: "))
#calculo el peso total de los payasos
peso_payasos = numero_payasos * peso_payaso
#calculo el peso total de las muñecas
peso_munecas = numero_munecas * peso_muñeca
#calculo el peso total del paquete
peso_total = peso_payasos + peso_munecas
#mostrar el peso total del paquete
print(f"El peso total del paquete es de : {peso_total} gramos")

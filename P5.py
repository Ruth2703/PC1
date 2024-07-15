#6
#defino el precio de la entrada por edad
infante = 0
niños = 5
adulto = 10
#Solicito cantidad de shows vistos
edad = int(input("¿Cuántos años tiene?: "))
#calculo precio de etrada por edad
if edad < 4:
    precio_entrada = infante
elif 4 <= edad <= 18:
    precio_entrada = niños
else:
    precio_entrada = adulto
#mostrar el valor de entrada
print(f"¿Precio de entrada?: ${precio_entrada}")



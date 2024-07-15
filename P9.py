#9
#definir lista
lista_original = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#posiciones a eliminar
posiciones_a_eliminar = [0, 4, 5]
# Crear una nueva lista sin los elementos en las posiciones especificadas
lista_filtrada = [elemento for i, elemento in enumerate(lista_original) if i not in posiciones_a_eliminar]
print(f"Lista original: {lista_original}")
print(f"Lista filtrada: {lista_filtrada}")

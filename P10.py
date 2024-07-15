#11
def eliminar_duplicados(lista):
# Convertir la lista a un conjunto (elimina duplicados)
  conjunto_sin_duplicados = set(lista)
  
  # Convertir el conjunto de vuelta a una lista (ordenada)
  lista_sin_duplicados = list(conjunto_sin_duplicados)
  return lista_sin_duplicados

# Ejemplo de uso
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")
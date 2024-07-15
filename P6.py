#7
def solicitar_numeros():
  numero_1 = float(input("Ingrese el primer número: "))
  numero_2 = float(input("Ingrese el segundo número: "))
  return numero_1, numero_2

while True:
  # Solicitar números
  numero_1, numero_2 = solicitar_numeros()

  # Mostrar menú y solicitar opción
  print("\nMenú de operaciones:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("0. Salir")
  opcion = int(input("Ingrese la opción deseada: "))

  # Realizar la operación seleccionada
  if opcion == 1:
    resultado = numero_1 + numero_2
    print(f"La suma de {numero_1} y {numero_2} es: {resultado}")
  elif opcion == 2:
    resultado = numero_1 - numero_2
    print(f"La resta de {numero_1} y {numero_2} es: {resultado}")
  elif opcion == 3:
    resultado = numero_1 * numero_2
    print(f"La multiplicación de {numero_1} y {numero_2} es: {resultado}")
  elif opcion == 0:
    print("¡Gracias por usar la calculadora!")
    break
  else:
    print("Opción inválida. Intente nuevamente.")



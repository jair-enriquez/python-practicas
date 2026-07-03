print("Bienvenido a la Calculadora Básica")
print("Alumno: Jair Enriquez Martinez") 
while True:
	entrada = input("Escriba la operación (+, -, *, /) o 'salir' para terminar: ").strip().lower()
	if entrada == "salir":
		print("ADIOS")
		break
	n1 = float(input("Introduce el primer número: "))
	n2 = float(input("Introduce el segundo número: "))
	if entrada == "+":
		res = n1 + n2
	elif entrada == "-":
		res = n1 - n2
	elif entrada == "*":
		res = n1 * n2
	elif entrada == "/":
		res = n1 / n2
	else:
		print("Operación no reconocida. Use +, -, *, / o 'salir'.")
		continue
	print(f"El resultado es: {res}")

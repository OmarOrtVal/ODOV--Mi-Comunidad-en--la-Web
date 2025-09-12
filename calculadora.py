num1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

if operador == '+':
    resultado = num1 + num2
    print(f"El resultado es: {resultado}")
elif operador == '-':
    resultado = num1 - num2
    print(f"El resultado es: {resultado}")
elif operador == '*':
    resultado = num1 * num2
    print(f"El resultado es: {resultado}")
elif operador == '/':
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print(f"El resultado es: {resultado}")
else:
    print("Operador inválido. Por favor, usa +, -, * o /.")
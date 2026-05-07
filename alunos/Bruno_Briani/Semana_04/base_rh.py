num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")

if num2 != 0:
    print(f"Divisão: {num1 / num2}")
else:
    print("Divisão: Não é possível dividir por zero.")
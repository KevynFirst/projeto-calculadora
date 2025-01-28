#!/usr/bin/env python3

# Inicia a calculadora
while True:
    print("Escolha a operação que deseja realizar:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Escolher a operação
    operacao = input("Digite o número da operação desejada: ")

    # Fechar a calculadora
    if operacao == "5":
        print("Saindo da calculadora...")
        break

    # Receber os 2 valores da operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação escolhida
    if operacao == "1":
        resultado = num1 + num2
        print(f"O resultado da soma é = {resultado}")

    elif operacao == "2":
        resultado = num1 - num2
        print(f"O resultado da subtração é = {resultado}")

    elif operacao == "3":
        resultado = num1 * num2
        print(f"O resultado da multiplicação é = {resultado}")

    elif operacao == "4":
        # Verifica se o divisor não é igual a zero
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é = {resultado}")
        else:
            print("Não é possível dividir um número por zero.")
    else:
        print("Operação inválida, tente novamente.")

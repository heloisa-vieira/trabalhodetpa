# -*- coding: utf-8 -*-
import os
import math
import random

# Função para realizar adição
def adicao():
    num1 = float(input("Digite o primeiro número para adição:"))
    num2 = float(input("Digite o segundo número para adição:"))
    soma = num1 + num2
    print(f"A soma de {num1} + {num2} é = {soma}")
    

    # Função para realizar subtração
def subtracao():
        num1 = float(input("Digite o primeiro número para subtração:"))
        num2 = float(input("Digite o segundo número para subtração:"))
        subtracao = num1 - num2
        print(f"A subtração de {num1} - {num2} é = {subtracao}")
    

        #Função para realizar multiplicação
def multiplicacao():
        num1 = float(input("Digite o primeiro número para multiplicação:"))
        num2 = float(input("Digite o segundo número para multiplicação:"))
        multiplicacao = num1 * num2
        print(f"A multiplicação de {num1} * {num2} é = {multiplicacao}")
    

        # Função para calcular divisão
def divisao():
        num1 = float(input("Digite o primeiro número para divisão:"))
        num2 = float(input("Digite o segundo número para divisão:"))
        if num2 == 0:
             print("ERRO: Divisão por zero não é permitida.")
        else:
             divisao = num1 / num2
             print(f"A divisão de {num1} / {num2} é = {divisao}")
             


# Função para calcular a raiz quadrada
def calcular_raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    if numero < 0:
        print("Número inválido para raiz quadrada")
    else:
        raiz = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {raiz}")
    input("Pressione qualquer tecla para continuar...")

# Função para calcular potência
def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"O resultado de {base} elevado a {expoente} é = {resultado}")
    input("Pressione qualquer tecla para continuar...")

# Função para gerar número randômico
def numero_aleatorio():
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    if inicio >= fim:
        print("O valor inicial deve ser menor que o valor final")
    else:
        numero = random.randint(inicio, fim)
        print(f"Número aleatório gerado entre {inicio} e {fim} é = {numero}")
    input("Pressione qualquer tecla para continuar...")

# Programa principal com menu
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Menu de funções matemáticas:")
        print("1. Calcular raiz quadrada")
        print("2. Calcular potência")
        print("3. Gerar número randômico")
        print("4. Realizar todas as operações básicas")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            calcular_raiz_quadrada()
        elif opcao == "2":
            potencia()
        elif opcao == "3":
            numero_aleatorio()
        elif opcao == "4":
            adicao()
            subtracao()
            multiplicacao()
            divisao()
            potencia()

        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            input("Pressione qualquer tecla para continuar...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            

if __name__ == "__main__":
    main()
                    
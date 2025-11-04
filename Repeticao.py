# -*- coding: utf-8 -*-

# Programa: Multiplicação interativa
import os

while True:
   
    # Solicita os dois números ao usuário
    os.system("cls")
    numero1 = float(input("Digite o primeiro número:"))
    numero2 = float(input("Digite o segundo número:"))

    # Calcula a multiplicação
    resultado = numero1 * numero2

    # Exibe o resultado
    print(f"\nO resultado da multiplicação de {numero1} x {numero2} é = {resultado}\n")

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja fazer outro calculo? (s/n)") .strip().lower()
    
    
    if continuar != 's':
        print("Fim do programa. Até logo!")
        break

    print("-" * 40) # Separador visual
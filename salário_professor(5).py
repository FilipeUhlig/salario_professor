"""
Programa: Salário do professor
Descrição: Este programa calcula o salário de um professor.
Autor: Filipe
Data: 04/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
h = float(input("Qual a quantidade de horas trabalhada? "))

#Processamento de dados
bruto = (h*40.00)
desconto = (bruto*(30/100))
liquido = (bruto - desconto)

#Saida de dados
print(f"Salário bruto: {bruto}")
print(f"Total de descontos de impostos: {desconto}")
print(f"Salário líquido: {liquido}")

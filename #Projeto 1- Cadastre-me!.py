#Projeto 1- Cadastre-me!

#Praticando

# ​# PROJETO 1 

## Objetivo de projeto
# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário
### Funcionalidades do módulo 1
'''
1. Obtenha o nome do usuário
2. Obtenha a idade do usuário
3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
'''
# cartoes = ['R$50,00','R$250,00','R$120,00']
'''
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
'''

# 1. Obtenha o nome do usuário

import datetime
import random

# Loop para validar o nome do usuário
while True:
    nome_usuario = input('Qual o seu nome? ')
    
    # Verifica se o nome não é vazio e contém apenas letras e espaços
    if nome_usuario.strip() == '':
        print("O nome não pode ser vazio. Tente novamente.")
    elif not nome_usuario.replace(' ', '').isalpha():
        print("O nome deve conter apenas letras e espaços. Tente novamente.")
    else:
        # Pergunta se o nome está correto
        confirmacao = input(f"Seu nome é '{nome_usuario}'. Está correto? (s/n): ").lower()
        
        if confirmacao == 's':
            break  # Sai do loop se o nome estiver correto
        elif confirmacao == 'n':
            print("Por favor, insira o nome novamente.")
        else:
            print("Resposta inválida. Responda com 's' para sim ou 'n' para não.")

# Após o nome ser validado e confirmado, exibe a mensagem final
print(f"Olá, {nome_usuario}!")

# Loop para validar a idade do usuário
while True:
    while True:
        try:
            idade = int(input('Qual a sua idade? '))
            if idade < 0:
                print("A idade não pode ser negativa! Tente novamente.")
            else:
                break  # Sai do loop se a idade for válida
        except ValueError:
            print("Erro! Por favor, insira um número válido para a idade.")

    # Pergunta ao usuário se a idade está correta
    confirmacao = input(f"Sua idade é {idade} anos. Está correta? (s/n): ").lower()

    if confirmacao == 's':
        break  # Sai do loop se a idade estiver correta
    elif confirmacao == 'n':
        print("Por favor, insira a idade novamente.")
    else:
        print("Resposta inválida. Responda com 's' para sim ou 'n' para não.")

# Após a confirmação da idade, o programa pode seguir
print(f"Sua idade confirmada é {idade} anos.")

# Obter a data atual
data_atual = datetime.date.today()

# Acessando diretamente os componentes da data (dia, mês, ano)
dia = data_atual.day
mes = data_atual.month
ano = data_atual.year

# Exibindo apenas a data formatada no formato DD-MM-YYYY
data_formatada = f"{dia:02d}-{mes:02d}-{ano}"

# Exibindo a data formatada
print(f"Data de hoje: {data_formatada}")

# Sorteio do cartão
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
valor_escolhido = random.choice(cartoes)

# Mensagens finais
print(f'Olá, {nome_usuario}, seu registro foi concluído com sucesso no dia {data_formatada}.')
print(f'Houve um sorteio e você ganhou um cartão de compras no valor de {valor_escolhido}. Parabéns!')




















  






















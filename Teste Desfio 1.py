## Sistema Bancário Desafio

## importando sistemas de cores
import colorama
from colorama import Fore as cor
## importando sistema de temporizador
import time


## Declaração de Variáveis
menu = cor.GREEN +'''
 *** MENU ***
 
[D] Deposito
[S] Saque 
[E] Extrato
[Q] Sair

 ************
 
''' + cor.RESET

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3



## Solicita nome do clinete para localização ficcticia e expõe as informações atuais
nome = input("Olá, digite seu nome para localizarmos sua conta: ")
print('Localizando conta...')
##timer
time.sleep(3)
print(f'\nBem vindo a sua conta {nome.upper() .strip()}, seu Saldo atual é de R${saldo}\n')


## Loop do menu e condições
while True:

    ## Loop do menu
     opcao = input(f'{menu}Seleciona a opção desejada: ').upper().strip()


    ## Loop de Depósito
     if opcao == "D":
        valor = float(input('\nDigite o valor que você quer depositar: R$'))

        ## Condição para o Depósito
        if valor > 0:
            print(cor.BLUE + 'Depósito Realizado com Sucesso' + cor.RESET)
            saldo += valor
            extrato += (cor.BLUE +f'\nDepósito: R${valor:.2f} \n' + cor.RESET)


        else:
         print(cor.RED + f'\n Operação inválida' + cor.RESET)

    ## Loop de Saques
     elif opcao == "S":
         valor = float(input(f'\nQual valor você deseja sacar? R$'))

         ## Variáves de condições para o saque
         excedeu_saldo = valor > saldo
         excedeu_limite = valor > limite
         excedeu_saques = numero_saques == LIMITE_SAQUES

         ## Mensagens de condições para o saque
         if excedeu_saldo:
             print(cor.RED + '\nFalha na Operação \nNão há saldo suficente para essa operação'+ cor.RESET)
         elif excedeu_limite:
             print(cor.RED +'\nFalha na Operação \nOperação excedeu o limite de R$500.00 por saque'+ cor.RESET)
         elif excedeu_saques:
             print(cor.RED +'\nFalha na Operação \nOpereação excedeu o limite de saques diário'+ cor.RESET)

         ## Condições para o saque
         elif valor > 0:
             print(cor.BLUE + 'Saque Realizado com Sucesso' + cor.RESET)
             saldo -= valor
             extrato += (cor.BLUE + f'\nSaque: R$ {valor:.2f}' + cor.RESET)
             numero_saques += 1


         else:
             print(cor.RED +'\nFalha na Operação \nValor inválido'+ cor.RESET)

         ## Loop de Extrato

    ## Loop de Extrato
     elif opcao == "E":
         print('Carregando Extrato...')
         time.sleep(3)
         print(cor.BLUE + "***Extrato***" + cor.RESET)
         print(cor.RED + 'Não foi realizada nenhuma movimentação.' if not extrato else extrato + cor.RESET)
         print(cor.BLUE + f'\n Saldo total em conta: R${saldo:.2f}' + cor.RESET)
         print(cor.BLUE +'*************' + cor.RESET)

    ## Encerramento do looping do MENU
     elif opcao == "Q":
         print(cor.BLUE + '\nObrigado por utilizar nosso Sistema'+ cor.RESET)
         time.sleep(1)
         break

         ##Linha de conteção de erros do MENU


     else: print(cor.RED + "Falha na Operação \nSelecione novamente uma opção válida" + cor.RESET)








#Adicionando biblioteca
from time import sleep
#Codigo Principal do Sistema Bancario desenvolvodp para o desafio do DIO

#Declaracao de variaveis Globais
saldo = 0
limite_saque = 0

#Declaracao de funcoes
def titulo(msg):
    titulo = f'{"="*54} \n{msg:^54} \n{"="*54}'
    return titulo


def vericaint(msg): #verifica se o numero digitado é um número inteiro
        num = None
        while num == None:
            try:
                num = int(input(f'{msg}'))
            except ValueError:
                print('\33[0;31mO valor digitado nao foi um número inteiro.\33[m')
            except KeyboardInterrupt:
                print('\n\33[0;31mO usuario preferiu nao digitar o numero.\033[m')
                return None
            except Exception as Erro:
                print(Erro.__class__)
            else: 
                return num
            
def menu(saldo, limite_saque = limite_saque):
    opc = 0
    print(titulo('Bem vindo ao Caixa Eletronico'))
    print(f"Saldo Disponível: {saldo:.2f}. \n\n"\
    "Digite uma das opções para continuar:\n\n" \
    "1 - Saque\n" \
    "2 - Deposito.\n" \
    "3 - Extrato.\n" \
    "4 - Sair.")

    while opc < 1 or opc > 4:
        opc = vericaint("\nOpcão desejada: ")
        if opc == 1:
            print('\n')
            saldo, limite_saque = saque(saldo, limite_saque)
            return saldo, limite_saque, False
        elif opc == 2:
            print('\n')
            saldo, limite_saque = deposito(saldo, limite_saque)
            return saldo, limite_saque, False
        elif opc == 4:
            print(titulo('Obrigado por utilizar nossos seriços. Volte Sempre!'))
            return saldo, limite_saque, True
            
            
        
        else:
            print('Opção invalída. Tente Novamente')
            return saldo, limite_saque


def saque(saldo, limite_saque):
    print(titulo('SAQUE'))
    print(f'Saldo Disponível: {saldo}\n')
    if limite_saque < 3:
        while True:
            saque = vericaint('Digite o valor que deseja sacar [0 para cancelar]\nR$')

            while saque < 0:
                print('\n\33[0;31mValor digitado é invalido.\033[m\n')
                saque = vericaint('Digite o valor que deseja sacar [0 para cancelar]\nR$')

                
            if saque == 0:
                print('Operacão cancelada.')
                saldo -= saque
                return saldo, limite_saque
            
            elif saque > 2000:
                print('\nNão é possível realizar saques maiores que R$2.000,00.')
                sleep(1)
                return saldo, limite_saque

            elif saldo > saque:
                saldo -= saque
                print('\nSaque realizado com sucesso.')
                limite_saque +=1
                sleep(1)
                return saldo, limite_saque
        
            
            else:
                print('\n\33[0;31mSaldo indisponível.\033[m\n')
    else:

        print('Limite de saque diário atingido, Tente Novamente amanhã.')
        return saldo, limite_saque
    



def deposito(saldo, limite_saque = limite_saque):

    print(titulo('DEPÓSITO'))
    print(f'Saldo Disponível: {saldo}\n')
    while True:
        deposito = vericaint('Digite o valor que deseja depositar [0 para cancelar].\nR$')

        while deposito  < 0:
            print('\n\33[0;31mValor digitado é invalido.\033[m\n')
            deposito = vericaint('Digite o valor que deseja depositar [0 para cancelar].\nR$')

        if deposito == 0:
            print('Operação cancelada.')
            return saldo, limite_saque

        else:
            saldo += deposito
            print('\nDeposito realizado com sucesso.')
            sleep(1)
            return saldo, limite_saque



#Corpo do Codigo

while True:
    saldo, limite_saque, sair = menu(saldo, limite_saque)

    if sair:
        break

    resp = input('\nDeseja realizar outra operação? [S/N]\n').upper()
    if resp == 'N':
        print(titulo('Obrigado por utilizar nossos seriços. Volte Sempre!'))
        break

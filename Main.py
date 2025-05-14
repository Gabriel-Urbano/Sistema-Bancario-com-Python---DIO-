#Adicionando biblioteca
from time import sleep

#Codigo Principal do Sistema Bancario desenvolvodp para o desafio do DIO

#Declaracao de variaveis Globais
saldo = 0
limite_saque = 0
extrato = list()

#Declaracao de funcoes
def titulo(msg):
    titulo = f'{"="*54} \n{msg:^54} \n{"="*54}'
    return titulo


def linha():
    print('-' * 54)

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
            
def menu(saldo, extrato, limite_saque = limite_saque):
    opc = 0
    print(titulo('Bem vindo ao Caixa Eletronico'))
    print(f"Saldo Disponível: R${saldo:.2f}. \n\n"\
    "Digite uma das opções para continuar:\n\n" \
    "1 - Saque\n" \
    "2 - Deposito.\n" \
    "3 - Extrato.\n" \
    "4 - Sair.")

    while opc < 1 or opc > 4:
        opc = vericaint("\nOpcão desejada: ")
        if opc == 1:
            print('\n')
            saldo, extrato, limite_saque = saque(saldo, extrato, limite_saque)
            return saldo, extrato, limite_saque, False
        elif opc == 2:
            print('\n')
            saldo, extrato, limite_saque = deposito(saldo, extrato, limite_saque)
            return saldo, extrato, limite_saque, False
        elif opc == 3:
            lerextrato(extrato)
            return saldo, extrato, limite_saque, False
        elif opc == 4:
            print(titulo('Obrigado por utilizar nossos seriços. Volte Sempre!'))
            return saldo, extrato,  limite_saque, True
        else:
            print('Opção invalída. Tente Novamente')
            return saldo, extrato, limite_saque, False


def saque(saldo, extrato, limite_saque):
    if limite_saque < 3:
        print(titulo('SAQUE'))
        print(f'Saldo Disponível: R${saldo:.2f}\n')
        while True:
            saque = vericaint('Digite o valor que deseja sacar [0 para cancelar]\nR$')

            if saque is None:
                print('Operacão cancelada.')
                saldo -= saque
                return saldo, extrato,  limite_saque
 
            elif saque == 0:
                print('Operacão cancelada.')
                saldo -= saque
                return saldo, extrato,  limite_saque
            
            elif saque < 0:
                print('\n\33[0;31mValor digitado é invalido.\033[m\n')
                continue
            
            elif saque > 2000:
                print('\nNão é possível realizar saques maiores que R$2.000,00.')
                sleep(1)
                continue

            elif saldo >= saque:
                saldo -= saque
                print('\nSaque realizado com sucesso.')
                extrato.append({'tipo': 'Saque', 'valor': saque, 'extsaldo' : saldo})
                limite_saque +=1
                sleep(1)
                return saldo, extrato, limite_saque

            else:
                print('\n\33[0;31mSaldo indisponível.\033[m\n')
    else:

        print('Limite de saque diário atingido, Tente Novamente amanhã.')
        return saldo, extrato, limite_saque
    



def deposito(saldo, extrato, limite_saque = limite_saque):

    print(titulo('DEPÓSITO'))
    print(f'Saldo Disponível: R${saldo:.2f}\n')
    while True:
        valor = vericaint('Digite o valor que deseja depositar [0 para cancelar].\nR$')

        if valor is None:
            print('Operação cancelada.')
            return saldo, extrato, limite_saque

        if valor  < 0:
            print('\n\33[0;31mValor digitado é invalido.\033[m\n')
            continue

        elif valor == 0:
            print('Operação cancelada.')
            return saldo, extrato, limite_saque

        else:
            saldo += valor
            print('\nDeposito realizado com sucesso.')
            sleep(1)
            extrato.append({'tipo': 'Depósito', 'valor': valor, 'extsaldo' : saldo})
            return saldo, extrato, limite_saque


def lerextrato(extrato):
    if not extrato: #Verifica se há algum extrato
        print('Não há transsações para exibir.')
    else:

        print(f'\n{titulo('Extrato')}')
        print(f'{'Tipo':<17}|{'Valor':<17}|{'Saldo':<17}|')
        
        for transacao in extrato:
            print(f'{transacao.get('tipo', ''):<17}|'\
            f'R$ {transacao.get('valor', '0'):<14.2f}|'\
            f'R$ {transacao.get('extsaldo'):<14.2f}|')
        linha()
       
    
#Corpo do Codigo

while True:
    saldo, extrato, limite_saque, sair = menu(saldo, extrato, limite_saque)

    if sair:
        break

    resp = input('\nDeseja realizar outra operação? [S/N]\n').upper()
    while resp not in 'NS':
        resp = input('\n\33[0;31mResposta invalida.\033[m\n'
        'Deseja realizar outra operação? [S/N]\n').upper()

    if resp == 'N':
        print(titulo('Obrigado por utilizar nossos seriços. Volte Sempre!'))
        break

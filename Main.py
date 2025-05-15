# Adicionando biblioteca
from time import sleep

# Declaracao de funcoes
def titulo(msg):
    titulo = f'{"="*54} \n{msg:^54} \n{"="*54}'
    return titulo


def linha():
    print('-' * 54)

def vericaint(msg): # verifica se o numero digitado é um número inteiro
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
            if num < 0:
                print('\33[0;31mEntrada inválida, digite um número positivo.\33[m')
                num = None
            else:
                return num


def verifcpf(msg):
    while True:
        cpf = input(f'{msg}')
        if cpf.isdigit():
            if len(cpf) == 11:
                return cpf
            else:
                print('\33[0;31mCPF inválido. O CPF precisa conter 11 digitos\033[m')
                continue
        else:
            print('\33[0;31mCPF inválido. Digite somente números.\033[m')
            continue


def verifnome(msg):
    nome = None
    while nome == None:
        try:
            nome = input(msg)
            for c in nome:
                if c.isdigit() or nome.strip() == '':
                    print('\33[0;31mValor invalido, somente é permito a entrade de letras. Tente novamente.\33[m')
                    nome = None
                    break
        except KeyboardInterrupt :
            print('\33[0;31m\nO usuario preferiu nao digitar.\33[m')
            nome = None
            break
        except Exception as erro:
            nome = None
        else:
            if nome != None:
                return nome.strip()


def menu():
    print(titulo('Bem vindo ao Caixa Eletronico'))
    print("\nDigite uma das opções para continuar:\n\n"
          "1 - Saque\n"
          "2 - Deposito.\n"
          "3 - Extrato.\n"
          "4 - Criar Usuario.\n"
          "5 - Criar conta corrente.\n"
          "6 - Sair.")
    while True:
        opc = vericaint("\nOpção desejada: ")
        if opc in [1, 2, 3, 4, 5, 6]:
            return opc
        else:
            print('Opção inválida. Tente Novamente')


def saque(*, saldo, extrato, limite_saque):
    if limite_saque < 3:
        print(titulo('SAQUE'))
        print(f'Saldo Disponível: R${saldo:.2f}\n')
        while True:
            saque_valor = vericaint('Digite o valor que deseja sacar [0 para cancelar]\nR$')

            if saque_valor is None:
                print('Operacão cancelada.')
                return saldo, extrato, limite_saque

            elif saque_valor == 0:
                print('Operacão cancelada.')
                return saldo, extrato, limite_saque

            elif saque_valor < 0:
                print('\n\33[0;31mValor digitado é invalido.\033[m\n')
                continue

            elif saque_valor > 2000:
                print('\nNão é possível realizar saques maiores que R$2.000,00.')
                sleep(1)
                continue

            elif saldo >= saque_valor:
                saldo -= saque_valor
                print('\nSaque realizado com sucesso.')
                extrato.append({'tipo': 'Saque', 'valor': saque_valor, 'extsaldo' : saldo})
                limite_saque +=1
                sleep(1)
                return saldo, extrato, limite_saque

            else:
                print('\n\33[0;31mSaldo indisponível.\033[m\n')
    else:
        print('Limite de saque diário atingido, Tente Novamente amanhã.')
        return saldo, extrato, limite_saque


def deposito(saldo, extrato):
    print(titulo('DEPÓSITO'))
    print(f'Saldo Disponível: R${saldo:.2f}\n')
    while True:
        valor = vericaint('Digite o valor que deseja depositar [0 para cancelar].\nR$')

        if valor is None:
            print('Operação cancelada.')
            return saldo, extrato

        if valor < 0:
            print('\n\33[0;31mValor digitado é invalido.\033[m\n')
            continue

        elif valor == 0:
            print('Operação cancelada.')
            return saldo, extrato

        else:
            saldo += valor
            print('\nDeposito realizado com sucesso.')
            sleep(1)
            extrato.append({'tipo': 'Depósito', 'valor': valor, 'extsaldo' : saldo})
            return saldo, extrato


def lerextrato(extrato):
    if not extrato: # Verifica se há algum extrato
        print('Não há transsações para exibir.')
    else:
        print(f'\n{titulo('Extrato')}')
        print(f'{"Tipo":<17}|{"Valor":<17}|{"Saldo":<17}|')

        for transacao in extrato:
            print(f'{transacao.get('tipo', ''):<17}|'
                  f'R$ {transacao.get('valor', '0'):<14.2f}|'
                  f'R$ {transacao.get('extsaldo'):<14.2f}|')
        linha()


def criar_usuario(lista, cpf_incluso = None):
    novo_usu = dict()
    print(titulo('Cadastro de novo cliente'))

    if cpf_incluso:
        print('CPF já está atribuido a conta.')
        cpf = cpf_incluso
    else:
        cpfs = [usuario["cpf"] for usuario in lista]
        cpf = verifcpf('Digite o CPF fo cliente: ')
        if cpf in cpfs:
            print('\33[0;31m\nCliente ja cadastrado.\033[m')
            return lista
        
    novo_usu['cpf'] = cpf
    nome = verifnome('Digite o nome do cliente: \n')
    novo_usu['nome'] = nome.title()

    print('Digite os seguintes dados do endereço do cliente:')
    endereco = input('Digire o logradouro: \n').title()
    nro = vericaint('Digite o número: \n')
    bairro = verifnome ('Digite o bairro: \n').title()
    cidade = verifnome('Digite o nome da cidade: ').title()
    estado = verifEstado()
    endereco = endereco + ' - ' + str(nro) + ' - ' + bairro + ' - ' + cidade + '/' + estado.upper()
    novo_usu['end'] = endereco

    lista.append(novo_usu)
    return lista


def verifEstado():
    estados_brasil = ["AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA",
                      "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ",
                      "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    while True:
        Estado = input('Digite  a sigla do estado [ex: SP]: ')
        if Estado.upper() in estados_brasil:
            return Estado
        else:
            print('\33[0;31mEstado inválido.\033[m')
            continue

def criar_conta_corrente(contas, usuarios):
    print(titulo('Cadastro de nova conta corrente'))
    cpf = verifcpf('Digite o CPF do proprietário: \n')
    usuario_por_CPF = {usuarios['cpf'] : usuario for usuario in usuarios}

    if cpf in usuario_por_CPF:
        usuario = usuario_por_CPF[cpf]
        usuario['contas'] = usuario.get('contas', [])
        contas+=1
        usuario['contas'].append(str(contas) + "/0001")
        print('Conta corrente criada com sucesso!')
        return usuarios, contas
    else:
        print('\33[0;31m\nCliente não cadastrado.\033[m')
        criar_novo = input('Deseja cadastrar este cliente agora? [S/N]: ').upper()
        if criar_novo == 'S':
            usuarios = criar_usuario(usuarios, cpf)  # Chama a função para criar o usuário ja com o cpf incluso
            # Tenta criar a conta corrente novamente após o cadastro
            usuario_por_CPF = {usuarios['cpf'] : usuario for usuario in usuarios}
            if cpf in usuario_por_CPF:
                usuario = usuario_por_CPF[cpf]
                usuario['contas'] = usuario.get('contas', [])
                contas+=1
                usuario['contas'].append(str(contas) + "/0001")
                print('Conta corrente criada com sucesso!')
                return usuarios, contas
            else:
                print('\33[0;31m\nErro ao criar conta corrente após o cadastro do usuário.\033[m')
                return usuarios
        else:
            print('\33[0;31m\nCadastro de conta corrente cancelado.\033[m')
            return usuarios

# Corpo do Codigo
def main():
    contas_existentes = 0
    saldo = 0
    limite_saque = 0
    extrato = []
    usuarios = []
    contas_corrente = []

    while True:
        opcao = menu()

        if opcao == 1:
            print('\n')
            saldo, extrato, limite_saque = saque(saldo = saldo,extrato = extrato, limite_saque = limite_saque)
        elif opcao == 2:
            print('\n')
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == 3:
            lerextrato(extrato = extrato)
        elif opcao == 4:
            usuarios, contas_existentes = criar_usuario(contas_existentes, usuarios)
        elif opcao == 5:
            contas_corrente = criar_conta_corrente(contas_corrente, usuarios)
        elif opcao == 6:
            print(titulo('Obrigado por utilizar nossos serviços. Volte Sempre!'))
            break

        resp = input('\nDeseja realizar outra operação? [S/N]\n').upper()
        while resp not in 'NS':
            resp = input('\n\33[0;31mResposta invalida.\033[m\n'
                         'Deseja realizar outra operação? [S/N]\n').upper()
        if resp == 'N':
            print(titulo('Obrigado por utilizar nossos serviços. Volte Sempre!'))

            break
        
if __name__ == "__main__":
    main()
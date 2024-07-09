
def menu():
    print ("Seja bem vindo escolha uma opcao:")
    menu = """ 
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [nu] Novo Usuario
    [cc] Criar Conta
    [lc] Listar Contas
    [0] Sair

    """
    return input(menu)
def depositar(saldo, valor, extrato,/):
    saldo += valor
    extrato += f"Depositou R${str(valor)}\n"
    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    '''
    if numero_saques == LIMITES_SAQUE:
        print ("Limites de saques exedido")
    else:          
        if valor <= 500 and valor <= saldo:
            saldo -= valor
            numero_saques += 1
            extrato += f"Sacou R${str(valor)}\n"
            #print(numero_saques)               
                
        else:
            print("valor invalido")
    ''' 

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def exbir_extrato(saldo, /, *, extrato):    
    if extrato == "":
        print("Sem movimentação")

def criar_usuario(usuarios):
    cpf = input("Informe seu cpf(somente numeros): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Ja existe esse usuario")
        return
    
    nome = input("Informe o nome do usuario: ")
    data_nascimento = input("Informa a data de nascimento (dd/MM//AAAA): ")
    endereco = input("Informe o endereco( Rua e Numero): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,"endereco": endereco})
    print("USUARIO CRIADO COM SUCESSO!!")

def filtrar_usuarios(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("CONTA CRIADA COM SUCESSO")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} 
    print("USUARIO NÃO ENCONTRADO!!")

def listar_contas(contas):
    for conta in contas:
        linha =f"""\
            Agencia:\t{conta['agencia']}
            C/c:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)

def main():
    LIMITES_SAQUE = 3
    LIMITES_ERRO = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""    
    numero_saques = 0    
    erros = 0
    usuarios = []
    contas = []
    


    while True:
        opcao = menu()
        if opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                 contas.append(conta)

        elif opcao == "lc":
           listar_contas(contas)
                        
        elif opcao == "1":
            print("Deposito")
            valor = float(input("Quanto: "))
            saldo, extrato = depositar(saldo, valor, extrato)            
            
        elif opcao == "2":
            print("Sacar")
            valor = float(input("Quanto: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato, 
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITES_SAQUE,
            )
            
        elif opcao == "3":
            exbir_extrato (saldo, extrato=extrato)
            print(f"Extrato\n{extrato}")
            print(f"Saldo = {saldo}")             
            
        elif opcao == "0" or erros == LIMITES_ERRO:        
            print("FINALIZADO")
            break
        else:
            print("OPCAO INVALIDA!!")
            erros +=1
    
        

main()
        



print ("Seja bem vindo escolha uma opcao:")
menu = """ 
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
LIMITES_SAQUE = 3
numero_saques = 0
LIMITES_ERRO = 3
erros = 0

while True:
    opcao = input(menu)
    if opcao == "1":
        print("Deposito")
        valor = int(input("Quanto: "))
        saldo += valor
        extrato += f"Depositou R${str(valor)}\n"
        
    elif opcao == "2":
        print("Sacar")
        if numero_saques == LIMITES_SAQUE:
            print ("Limites de saques exedido")
        else:                
            valor = int(input("Quanto: "))
            if valor <= 500 and valor <= saldo:
                saldo -= valor
                numero_saques += 1
                extrato += f"Sacou R${str(valor)}\n"
                #print(numero_saques)               
            
            else:
                print("valor invalido")
    elif opcao == "3":
        print(f"Extrato\n{extrato}")
        print(f"Saldo = {saldo}")
        if extrato == "":
            print("Sem movimentação")
    elif opcao == "0" or erros == LIMITES_ERRO:        
        print("FINALIZADO")
        break
    else:
        print("OPCAO INVALIDA!!")
        erros +=1

        
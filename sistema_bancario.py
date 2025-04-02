user = str(input("Digite o seu usuario: "))
extrato = float()
op = -1
while op != 0:
    op = int(input(f"""
    
        Qual operação você deseja:   R$: {extrato:.2f}    
          [1] Depositar                    
          [2] Extrato                      
          [3] Saque                        
          [0] Fechar                       
             
"""))
    if op == 1:
        deposito = float(input("Digite o valor que deseja depositar: "))
        extrato += deposito       
        print(f"Operação concluida \n +{deposito:.2f}")

    elif op == 2:
        print(f"o Extrato da sua conta é de: {extrato:.2f}")

    elif op == 3:
        saque = float(input("Digite o valor que deseja sacar: "))
        extrato -= saque
        print(f"Operação concluida \n -{saque:.2f}")

print(f"Operação finalizada \n Extrato total: {extrato:.2f}")


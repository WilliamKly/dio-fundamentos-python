from datetime import datetime


menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

==>
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:

  op = input(menu)

  if op == "d" or op == "D":
    valor = float(input("Digite o valor a ser depositado: "))
    saldo += valor
    print(f"Depósito de R$ {valor} realizado com sucesso!")
    print(f"Seu saldo agora é de R$ {saldo}")
    data_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    extrato.append({"acao": "Depósito", "valor" : valor, "data": data_formatada})

  elif op == "s" or op == "S":
    saque = float(input("Digite o valor a ser sacado: "))
    if saque > saldo:
      print(f"Saldo insuficiente, seu saldo é de R$ {saldo}")
    else:
      if numero_saques == LIMITE_SAQUES:
        print("Você atingiu o limite de saques diários")
      elif limite < saque:
        print("Você ultrapassou o seu limite por saque")
      else:
        saldo -= saque
        print(f"Saque de R$ {saque} realizado com sucesso")
        numero_saques += 1
        data_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append({"acao": "Saque", "valor": saque, "data": data_formatada})
    
  elif op == "e" or op == "E":
    print("=== EXTRATO DA CONTA ===")
    for item in extrato:
      print(f"Ação: {item['acao']} --- Valor: R$ {item['valor']} --- Data: {item['data']}")

  elif op == "q" or op == "Q":
    print("Finalizando...")
    break

  else:
    print("Opção inválida, digite novamente")
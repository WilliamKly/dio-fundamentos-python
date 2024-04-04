from datetime import datetime

menu = """

[u] - Cadastrar usuário
[c] - Criar conta
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

==>
"""

usuarios = []
contas = []
extrato_conta = []
numero_conta = 1
LIMITE_SAQUES = 3

def criar_conta(usuario, saldo_inicial=0):
  global numero_conta
  for user in usuarios:
    if not user["cpf"] == usuario:
      return print("Essa conta não existe!")
  conta = {"numero_conta": numero_conta, "usuario": usuario, "saldo": saldo_inicial}
  contas.append(conta)
  numero_conta += 1
  return conta

def criar_usuario(nome, data_nascimento, cpf, endereco):
  for usuario in usuarios:
    if usuario["cpf"] == cpf:
      print("Usuário já existe no sistema")
      return None
  novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
  usuarios.append(novo_usuario)
  return novo_usuario

def buscar_conta(cpf):
  for conta in contas:
    if conta["usuario"] == int(cpf):
      return conta
  return None

def depositar(saldo, valor):
  saldo += valor
  print(f"Depósito de R$ {valor} realizado com sucesso!")
  print(f"Seu saldo agora é de R$ {saldo}")
  data_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  extrato_conta.append({"acao": "Depósito", "valor": valor, "data": data_formatada})
  return saldo, extrato_conta

def sacar(*, saldo, valor, extrato_conta, limite):
  if valor > saldo:
    print(f"Saldo insuficiente, seu saldo é de R$ {saldo}")
  else:
    if len([item for item in extrato_conta if item['acao'] == 'Saque']) >= LIMITE_SAQUES:
      print("Você atingiu o limite de saques diários")
    elif limite < valor:
      print("Você ultrapassou o seu limite por saque")
    else:
      saldo -= valor
      print(f"Saque de R$ {valor} realizado com sucesso")
      data_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      extrato_conta.append({"acao": "Saque", "valor": valor, "data": data_formatada})
  return saldo, extrato_conta

def extrato(*, extrato_conta, cpf):
  print(f"=== EXTRATO DA CONTA DE CPF {cpf} ===")
  for item in extrato_conta:
    print(f"Ação: {item['acao']} --- Valor: R$ {item['valor']} --- Data: {item['data']}")

while True:
  op = input(menu)

  if op.lower() == "u":
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DIA-MES-ANO): ")
    cpf = int(input("Digite o CPF do usuário: "))
    endereco = input("Digite o endereço do usuário: ")
    criar_usuario(nome, data_nascimento, cpf, endereco)
    print("Usuário cadastrado com sucesso")

  elif op.lower() == "c":
    usuario = int(input("Digite o cpf do usuário: "))
    criar_conta(usuario)
    
  elif op.lower() == "d":
    valor = float(input("Digite o valor a ser depositado: "))
    cpf = input("Digite o CPF do usuário: ")
    conta = buscar_conta(cpf)
    if conta:
      conta["saldo"], extrato_retorno = depositar(conta["saldo"], valor)
      conta["extrato"] = extrato_retorno
    else:
      print("Conta não encontrada.")
  
  elif op.lower() == "s":
    valor = float(input("Digite o valor a ser sacado: "))
    cpf = input("Digite o CPF do usuário: ")
    conta = buscar_conta(cpf)
    if conta:
      conta["saldo"], extrato_retorno = sacar(saldo=conta["saldo"], valor=valor, extrato_conta=extrato_conta, limite=500)
      conta["extrato"] = extrato_retorno
    else:
      print("Conta não encontrada.")

  elif op.lower() == "e":
    cpf = input("Digite o CPF do usuário: ")
    conta = buscar_conta(cpf)
    if conta:
      extrato(extrato_conta=conta["extrato"], cpf=conta["usuario"])
    else:
      print("Conta não encontrada.")

  elif op.lower() == "q":
    print("Finalizando...")
    break

  else:
    print("Opção inválida, digite novamente")

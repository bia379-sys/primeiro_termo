# # # 1. O Problema da Idade
# # idade = input("Digite sua idade: ")
# # if idade >= 18:
# # print("Você é maior de idade.")
# # Corrigido
# idade = input("Digite sua idade: ")
# if idade > "18":
#     print(f"Você é maior de idade.")
# # Melhorado
# idade = input("Olá digite sua idade: ")
# if idade > "18":
#     print(f"Você é maior de idade.")
# elif idade < "18":
#     print(f"Você é menor de idade.")

# # 2. A Escrita Fiel
# # nome = "Mariana"
# # print("Seja bem-vinda, nome!")
# # Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")
# # Melhorado
# nome = input("Qual é o seu nome?: ")
# print(f"Olá {nome} seja bem vinda")

# # 3. Falta de Espaço
# # numero = 10
# # if numero > 5:
# # print("O número é maior que cinco.")
# # else:
# # print("O número é menor ou igual a cinco.")
# # Corrigido
# numero = 10
# # if numero > 5:
# #     print("O número é maior que cinco.")
# # else:
# #     print("O número é menor ou igual a cinco.")
# # Melhorado
# numero = input("Qual é o número?: ")
# if numero > "5":
#     print("O número é maior que 5")
# else:
#     print("O número é menor que 5")

# # 4. Esquecimento Fatal
# # usuario = "aluno123"
# # if usuario == "aluno123"
# # print("Login realizado com sucesso.")
# # Corrigido
# # usuario = "aluno123"
# # if usuario == "aluno123":
# #     print("Login realizado com sucesso.")
# # Melhorado
# usuario = input("Qual é a senha de usúario?: ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
# else:
#     print("Senha incorreta tente novamente")

# # 5. Atribuição vs. Comparação
# # clima = "ensolarado"
# # if clima = "chuvoso":
# # print("Leve um guarda-chuva!")
# Corrigido
# clima = "chuvoso"
# if clima == "chuvoso":
#     print(f"Leve um guarda-chuva!")
# # Melhorado
# clima = input("Como está o dia hoje?: ")
# if clima == "chuvoso":
#     print(f"Leve um guarda chuva e tome cuidado!")
# else:
#     print(f"Aproveite o dia!")


# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")
# Corrigido
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")
# Melhorado
# pontos = input("Quantos pontos você fez?: ")
# print(f"Parabéns! Você fez {pontos} pontos.")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")
# Corrigido
# nota = "9.5"
# if nota >= "9":
#     print(f"Excelente!")
# elif nota >= "7":
#     print(f"Aprovado")
# Melhorado
# nota = input("Qual foi a nota tirada?: ")
# if nota >= "9":
#     print(f"Sua nota foi excelente!")
# elif nota >= "6":
#     print(f"Você foi aprovado")
# else:
#     print(f"Você pode melhorar!")   


# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)
# Corrigido
# for i in range(6):
#  print(i)
# Melhorado
# print("Será iniciada a contagem regressiva")
# for i in range(6):
#  print(i)


# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas
# Corrigido
# tentativas = 1
# while tentativas <= 3:
#     tent = int(input("Digite a quantidade"))
#     for tentativas in range(tent):       
#         print("Tentando conectar...") 
    # break
#  O código deveria parar após 3 tentativas
# Melhorado
# tentativas = 1
# while tentativas <= 3:
#  print("Tentando conectar...")
#  tentativas += 1
# print("Tentativas esgotadas. Conexão falhou.")


# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")
# Corrigido
# senha = input(f"Digite a senha secreta: ")
# while senha == "python123":
#    print("Acesso concedido!")
#    break
# # Melhorado
senha = input(f"Olá! digite a senha secreta: ")
while senha == "python123":
   print("Acesso concedido!")
   break
else:
   print("Senha incorreta tente novamente!")

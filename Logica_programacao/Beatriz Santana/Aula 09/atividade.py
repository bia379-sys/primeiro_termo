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

# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")
# Corrigido
# clima = "chuvoso"
# if clima == "chuvoso":
#     print(f"Leve um guarda-chuva!")
# Melhorado
clima = input("Como está o dia hoje?: ")
if clima == "chuvoso":
    print(f"Leve um guarda chuva e tome cuidado!")
else:
    print(f"Aproveite o dia!")

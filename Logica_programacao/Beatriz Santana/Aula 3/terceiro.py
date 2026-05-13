# Lógicas e Decisões 
# Se condição verdadeira
# Se condição ainda verdadeira porém críterios
# Senao condição falsa 
# if elif e else
# Sinais de > < =

# Exemplo 1
print("verificar idade")
idade = int(input("Digite sua idade "))

if idade >=18 :
    print("Você é maior de idade")
elif idade >= 16:
    print("Você não é de maior porém pode votar")
else:
    print("Você não é de maior")

# Exemplo 2 
# Valores 
print("Checar valores")
valor = int(input("Digite um valor"))

if valor > 100: 
    print("Valores acima de 100")
    print("O valor é", valor + 1) # pode-se mudar o "+" para qualquer outro símbolo de equação

else:
    print("Valores abaixo de 100")
    print("O valor é", valor - 1)

# Exemplo 3
# Criar um algoritmo que permita escolher a opção
print("Menu de Opção")
print ("Escolha uma das opções")
print("Filmes F e Séries S e X para Sair")

escolha = input("Digite uma opção")

if escolha == "F":
    print("Você escolheu Filmes")
elif escolha == "S":
    print(" Você escolheu Séries")
else: 
    print("Você saiu do programa")

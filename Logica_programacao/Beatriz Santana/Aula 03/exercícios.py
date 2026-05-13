# Exercício 1 
# Criar um algoritmo para realizar a locação de filmes ou séries seguir o modelo anterior. Ao escolher a opção você deverá perguntar o nome do cliente do filme ou série e quantidade que deseja assim como o valor de aluguel
# Para filmes R$ 5,00 e para séries R$ 10,00 

print("Olá, aqui fazemos locações de filmes e séries")
print ("Temos diversas opções de FIlmes e Séries  escolha entre as opções")
print("Filmes F e Séries S e X para Sair")

escolha = input("Digite uma opção")

if escolha == "F":
    print("Você está na sessão filmes")
    nome = input("Digite seu nome")
    filmes = input("Qual filme você deseja?")
    qtde = int(input("Qual quantidade deseja?"))
    valor = 5
    total = qtde * valor
    print("Parábens pela sua locação:", nome)
    print("O filme que você escolheu foi:", filmes)
    print("Quantidade de vezes que você pode assistir:", qtde)
    print("O valor da locação é:", valor)
    print("O total da sua locação foi:", total)
elif escolha == "S":
    print(" Você escolheu Séries")
    nome = input("Digite seu nome")
    Séries = input("Qual série você deseja?")
    qtde = int(input("Qual quantidade deseja?"))
    valor = 10
    total = qtde * valor
    print("Parábens pela sua locação:", nome)
    print("A série que você escolheu foi:", Séries)
    print("Quantidade de vezes que você pode assistir:", qtde)
    print("O valor da locação foi de:", valor)
    print("O total da sua locação foi:", total)
else: 
    print("Você saiu do programa")

# Exercicíos 2
# Loja de Comidas e Doces
# Criar um algoritmo para compra de produtos
# 1 - Comida
# 2 - Bebida
# 3 - Doces
# Ao escolher as opções cada um terá um valor de porcentagem, comida = 10%, bebida = 5% e Doces = 2%

print("Olá, você gostaria de comprar comida, bebida ou doces?")
escolha = input("Digite uma opção")
if escolha == "comida":
    valor = int(input("Qual valor você vai gastar?")) 
    desconto = valor * 10 / 100 
    total = valor - desconto
    print("O total da compra com desconto será de:", total)
elif escolha == "bebida": 
    valor = int(input("Qual valor você vai gastar?")) 
    desconto = valor * 5 / 100 
    total = valor - desconto
    print("O total da compra com desconto será de:", total)
elif escolha == "doces":
    valor = int(input("Qual valor você vai gastar?")) 
    desconto = valor * 2 / 100 
    total = valor - desconto
    print("O total da compra com desconto será de:", total) 
else: 
    print("Você saiu do programa")

# Exercicío 3
# Calculadora com operadores
# Sua calculadora deverá perguntar qual operador ele deseja e calcular os valores desejados. 
print("Olá, essa é a calculadora com operações")
print("Qual operação você deseja fazer?")
print("Digite A para Adição, S para Subtração, M para Multiplicação e D para divisão")
escolha = input("Digite uma opção")
if escolha == "A":
    valorA = int(input("Qual o primeiro valor que você deseja calcular?"))
    valora = int(input("Qual o segundo valor?"))
    total = valorA + valora
    print("O resultado da operação é:", total)
elif escolha == "S":
    valorS = int(input("Qual o primeiro valor que você deseja calcular?"))
    valors = int(input("Qual o segundo valor?"))
    total = valorS - valors
    print("O resultado da operação é:", total)
elif escolha == "M":
    valorM = int(input("Qual o primeiro valor que você deseja calcular?"))
    valorm = int(input("Qual o segundo valor?"))
    total = valorM * valorm
    print("O resultado da operação é:", total)
elif escolha == "D":
    valorD = int(input("Qual o primeiro valor que você deseja calcular?"))
    valord = int(input("Qual o segundo valor?"))
    total = valorD / valord
    print("O resultado da operação é:", total)

# Exercício 4
# Calculo de Notas
# Nossas atividades são por base de cálculo em somativa 1 e somativa 2, no final temos uma média.
# Acima ou igual a 50 o aluno será aprovado caso contrario reprovado 
# O programa deverá perguntar o nome e as notas e apresentar o resultado final do aluno
print("Calculo de Notas- Senai")
print("Somativas do primeiro semestre")
p1 = float(input("Digite a nota somativa 1: \n"))
p2 = float(input("Digite a nota somativa 2: \n"))
ptotal = (p1+p2) / 2
print("As somativas do primeiro semestre são: \n", round(ptotal,2))
print("Somativas do segundo semestre")
s1 = float (input("Digite a nota somativa 1: \n"))
s2 = float(input("Digite a nota somativa 2: \n"))
ptotal = (s1+s2) / 2
print(" As somativas do segundo semestre são: \n", round(ptotal,2))
if ptotal >=50 :
    print("Você foi aprovado!")
else:
    ptotal <=50 
    print("Você foi reprovado!")

# Exercício 5
# Criar um algoritmo para calcular uma viagem de carro, ônibus e avião
# Viagens de carro: Deve ser feito um abastecimento e deve cobrar o valor do pedágio
# Ônibus: Deve ser cobrado o valor da passagem e o valor do seguro de 3,88
# Avião: Cobrar o valor da viagem e valor de taxa de embarque 55,20
print("Olá, nós iremos calcular qual será o valor da sua viagem")
print("Qual meio de transporte será utilizado? Ônibus, Avião ou Carro?")
escolha = input("Digite uma opção")
if escolha == "Ônibus":
    ps = int(input("Qual o valor da passagem?"))
    print("Será cobrado um valor fixo do seguro de 3,88")
    total = ps + 3,88
    print("O valor gasto é:", total)
elif escolha == "Avião":
    av = int(input("Qual o valor da passagem?"))
    print("Será cobrado um valor fixo do seguro de 55,20")
    total = av + 3,88
    print("O valor gasto é:", total)
elif escolha == "Carro":
    cr = int(input("Qual valor de combustível será adicionado?"))
    cro = int(input("Qual o valor de pedágio que será pago?"))
    total = cr + cro
    print("O valor gasto é:", total)

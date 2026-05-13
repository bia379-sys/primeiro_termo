# Questão 1:
print("Registro de veículo")
modelo = input("Qual é o modelo do veículo?...")
placa = input("Qual é a plaaca do veículo?...")
print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")


# Questão 2:
print("Cálculo de Autonomia")
tanque = float(input("Qual é a capacidade do seu tanque em Litros"))
consumo = float(input("Digite o consumo médio por caminhão em Km/L"))
total = tanque / consumo
print(f"Seu caminhão pode percorrer {total:.2f} em Km/l")
print("Seu caminhão pode percorrer", round(total,2), "em Km/l")


# Questão 3:
print("Conversor de moeda (Frete internacioanal)")
valor_reais = float(input("Qual é o valor em Reais que será convertido?..."))
taxa_dolar = float(input("Qual é o valor da taxa do dolar em reais?..."))
total = valor_reais / taxa_dolar
print(f"O valor total convertido é... {total:.2f}")

# Questão 4:
print("Média de Entrega")
tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
tempo3 = int(input("Qual foi o tempo para concluir a fota 3 em horas"))
media = (tempo1 + tempo2 + tempo3) / 3
print(f"A media {media:.2f} de tempo das entregas ")


# Questão 5:
print("Monitor de Carga")
peso = float(input("Qual é o peso atual do seu caminhão?..."))

if peso < 10:
    print("Carga leve")
elif peso <= 25:
    print("Carga padrão")
else:
    print("ALERTA: Excesso de peso!")


# Questão 6:
print("Classificador de Destino")
print("regiões = N - Região Norte, S - Região Sul, Qualquer outra - Internacional")
#.lower() > minúsculo / .upper() > maiúsculo = Vai ler a resposta mesmo ela sendo maiúscula/minúscula
regiao = input("Inserir o código da Região: ").lower()
if regiao == "N":
    print("Região Norte")
elif regiao == "S":
    print("Região Sul")
else:
    print("Região Internacional")


# Questão 7:
print("Liberação de Saída") 
checklist = input("O checklist foi concluído? [Concluído ou Não Concluído]")
motorista = input("O motorista foi indentificado? [Sim ou Não]")
if checklist == "Concluído" and motorista == "Sim":
    print("Veículo autorizado a iniciar rota.")
else:
    print("Veículo NÃO autorizado a iniciar rota. Verificar checklist e identificação do motorista.")


# Questão 8:
print("Cálculo de atrasos")
total_entregas = int(input("Total de Entregas Agendadas:..."))
total_atrasos = int(input("Total de Entregas em Atrasos:..."))
if total_atrasos > total_entregas/0.1:
    print("Necessário otimizar")
else: 
    print("Logística Eficiente")


# Questão 9:
print("Validação de Calibragem")
pressao = float(input("Digite a pressão do pneu em PSI:..."))
if 100 <= pressao <= 110:
    print("Dentro do padrão")
elif pressao < 100:
    print("Abaixo do recomendado")
else:
    print("Acima do recomendado")


# Questão 10:
print("Contagem de Embarque")
import time
for contagem in range(5,0,-1):
    time.sleep(1)
    print(contagem)
print("Portão Trancado")


# Questão 11:
print("Somatório de Frete (Acumulador)")
total = 0
while True:
    valor = float(input("Valor do Frete: "))
    if valor == 0:
        total += valor
        print(f"Total acumulado {total} do frete ") 
    print("Fim do cálculo de fretes. ")

print("Somatório de Frete (Acumulador) - Versão 2")
faturamento_total = 0
valor_frete = -1
while valor_frete != 0:
    valor_frete = float(input("Valor do frete ou 0 para encerrar"))
    faturamento_total += valor_frete
    print(f"Faturamento acumulado: R$ {faturamento_total}")
print("Cálculo executado com sucesso")


# Questão 12
print("Monitoramento de Frota")
maior_km = 0
for frota in range(1, 6):
    km = float(input(f"Digite a quilometragem do veículo {frota}: "))
    if km > maior_km:
        maior_km = km
print(f"A maior quilometragem registrada é: {maior_km} km.")


# Questão 13:
print("Sistema de Rastreio")
codigo_correto = "track99"
tentativas = 0
max_tentativas = 3
while tentativas < maxtentativas:
    codigo_input = input("Código de acesso para o rastreador: :)")
    if codigo_input == codigo_correto:
        print("Acesso permitido. Iniciando rastreamento...")
        break
    else:
        tentativas += 1
        print("Acesso negado")
        if tentativas < max_tentativas:
            print(f"Tentativas restantes: {max_tentativas-tentativas}")
else:
    print("Rastreamento Bloqueado")

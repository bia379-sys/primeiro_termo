# Atividade 1: Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"
modelo = input("Olá! Qual é o modelo do seu veículo?: ")
placa = input("Qual é a placa do seu veículo?: ")
print(f"O veículo de modelo {modelo} e de placa {placa} está registrado no sistema. Boa Viagem!")


#Atividade 2: Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
#o consumo médio do caminhão (km/l).
#○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
#cheio.
combustivel = float(input("Qual é a capacidade do tanque de combustível em litro?: "))
consumo = float(input("Qual é o consumo médio dele por km rodado?: "))
total = combustivel / consumo
print(f"A distância total que o veículo pode percorrer com o tanque cheio é {total} km")


# Atividade 3: Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.
real = float(input("Quantos reais você gostaria de converter?: "))
dolar = float(input("Quanto reais o dolar está custando atualmente?: "))
conversão = real / dolar
print(f" A conversão do valor de reais é de $ {conversão} USD")


# Atividade 4: Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.
rota1 = float(input("Quantas horas são gastas na rota 1?: "))
rota2 = float(input("Quantas horas são gastas na rota 2?: "))
rota3 = float(input("Quantas horas são gasta na rota 3?: "))
total = rota1 + rota2 + rota3 / 3
print(f" A média de tempo gasta é de {total} h ")

# # Atividade 5: Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# # ○ Abaixo de 10t: "Carga Leve".
# # ○ Entre 10t e 25t: "Carga padrão".
# # ○ Acima de 25t: "ALERTA: Excesso de Peso!".
peso = int(input("Qual é o peso atual do caminhão em toneladas?"))
if peso <=10 :
    print("Carga leve")
elif peso <=25 :
    print("Carga padrão")
else:
    print("ALERTA: Excesso de Peso!")


# # Atividade 6: Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# # "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# # Internacional".
destino = input("Qual é a letra inicial do código da carga?: ")
if destino == "N":
    print("Região Norte")
elif destino == "S":
    print("Região Sul")
else:
    print("Região Internacional")


# # Atividade 7: Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# # motorista_identificado == "sim".
# # ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.
caminhão = input("Qual é o estado do checklist do caminhão?: ")
motorista = input("O motorista foi identificado?: ")
if caminhão =="concluído" and motorista =="sim":
    print("Motorista e checklist concluídos. Veículo autorizado a iniciar rota")
else:
    print("Liberação não autorizada")


# Atividade 8: Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente"
print("Olá! Faremos um cálculo de atrasos de entrega")
agendadas = int(input("Qual é o total de entregas agendadas?: "))
atrasos = int(input("Qual é o total de entregas realizadas com atraso?: "))
entregastotais = agendadas + atrasos
percentual = entregastotais * 0.1
if entregastotais >= percentual: 
    print("Necessário otimizar")
else: 
    print("Logística eficiente")


# Atividade 9: Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.
print("Olá! vericaremos se a calibragem está dentro do padrão")
pressão = float(input("Qual é a pressão do pneu em PSI?: "))
if pressão <= 100:
    print("Quantidade abaixo do recomendado. Por favor calibre o pneu")
elif pressão >= 110:
    print("Quantidade acima do recomendado. Por favor diminuia a calibragem do pneu")
else: 
    print("Medida dentro do padrão. Boa viagem!")

# Atividade 10: Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
print("Será iniciada a contagem regressiva para o fechamento dos portões")
import time 
contagem = [1, 2, 3, 4, 5]
for fim in contagem:
    while fim == 5:
        time.sleep(5)
        break
print("Contagem regressiva finalizada. Portão Trancado!")

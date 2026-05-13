# # Exercício 1
# # Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 
# # (simulando uma falha de sensor específica no item 5)

# for sensor in range (1,11):
#       if sensor == 5:
#         print(f"Sensor n° {sensor} com falha")
#       print(f"Sensor {sensor} sem falha")
#       continue
# print("Fim ;)")

# # Exercício 2
# # Simule um semáforo com parada para cada cor. 
# # Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor. 
# # Use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela).
# #cores = ["Verde", "Amarelo", "Vermelho"]
# #for cor in cores: 
# #    if cor == "Amarelo":
# #        print(f"O sinal {cor} defeito")
# #    print(f"O sinal {cor} está em funcionamento")
# import time
# cores = ["Verde", "Amarelo", "Vermelho"]
# for cor in cores:
#     if cor == "Amarelo":
#         print(f"Semáforo com defeito, pulando a cor {cor}...")
#         continue # Pula a cor amarela
#     print(f"Semáforo na cor {cor}. Parando por 3 segundos...")
#     time.sleep(3) #simula a pausa para cada cor 
# print("Fim do ciclo do semáforo")

# # Exercicio 3 - Soma de Cargas de Energia (for)
# # Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kwh de cada uma das 5 máquinas. 
# # Ao final do loop, o programa deve exibir o consumo tota da fábrica.
# consumo = 10
# for maq in range(1,6): 
#     aqm = float(input(f"Digite o valor que da máquina {maq} n°"))
#     consumo += aqm
#     print("Total da soma das máquinas", {consumo})

# #Exercício 4 - Identificador de Peças Defeituosas (for+if)
# #Percorra uma lista de medidas de peças:
# # medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# # O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# # Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada"
# print("Faremos a avaliação das peças de acordo com o padrão de qualidade da empresa.")
# pecas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for medida in pecas:
#     if medida >= 50.0:
#      print(f"Peça com medida de {medida}mm: aprovada!")
#     else: 
#      print(f"Peça com medida {medida}mm: rejeitada.")
# print("Fim da avaliação de peças.")

# Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. 
# O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# Crie um programa que peça ao usuário o peso de cada saco (via input dentro do loop) e, para cada um, informe se ele está "Dentro do limite" (entre 48kg e 52kg) ou "Fora do limite". 
# No final, exiba quantos sacos estão dentro do limite

escolha = float(input("Qual é o peso do saco?"))
for peso in range(1,7):
   if 48 < peso <=  50.0:
      print(f"Saco com peso {peso}kg: aprovado")
   else: 
      print(f"Saco com peso {peso}kg: Reprovado")
print("Fim da avaliação.")
# Exercicio 1 
# Criar um algoritmo, pergunte essas informações: seu nome, idade, curso e seu hobbie e apresente no final o resultado
pi1 = input("Qual é o seu nome?: \n")
pi2 = int(input("Qual é a sua idade?: \n"))
pi3 = input("Qual é o seu curso?: \n")
pi4 = input("Qual é o seu hobbie?: \n")
print ("Suas informações:", pi1, pi2, pi3, pi4)
# # Exercicio 2
# # Criar um algoritmo que pergunte o valor A e o valor B apresente o resultado em um valor C
pv1 = int(input("Qual é o valor de A?:, \n"))
pv2 = int(input("Qual é o valor de B?:, \n"))
print("O valor de C é:",pv1+pv2)
# # Exercicio 3 
# # Criar um algoritmo calcule sua viagem por 3 pedágios, em cada pedágio será cobrado um valor e no fim apresente o total das passagens
pd1 = int(input("Qual é o valor do pedágio 1?:, \n"))
pd2 = int(input("Qual é o valor do pedágio 2?:, \n"))
pd3 = int(input("Qual é o valor do pedágio 3?:, \n"))
print("O valor total da passagem é:",pd1+pd2+pd3)
# Exercico 4
# Criar um algoritmo para calcular IMC (Indice de Massa Corporal).
ps = float(input("Qual é a sua peso?, \n"))
alt = float(input("Qual é a sua altura?, \n"))
print("O seu IMC é:", ps/(alt*alt))
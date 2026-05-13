# Criar um algoritmo para que: 

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

# entrada
tag_ticket = input(f"Olá você usará a Tag ou o Ticket ?: ")
placa = input(f"Qual é a placa do carro?: ")
entrada = int(input(f"Qual foi o horário de entrada do veículo?: "))
if tag_ticket == "Tag":
    print("Aguarde o levantamento da catraca")
elif tag_ticket == "Ticket":
    print("Aperte o botão para retirada do ticket e Aguarde o levantamento da catraca")

# saída
print(f"Olá o valor é de 12 Reais por hora \n Placa do veículo: {placa} \n Horário de entrada: {entrada} \n Forma de pagamento: {tag_ticket} ")
saida = int(input("Qual é o horário de saída?: "))
valor_total = entrada - saida
if tag_ticket == "Tag":
    print(f"O valor de {valor_total} será debitado da sua conta Obrigada pela preferência volte sempre!")


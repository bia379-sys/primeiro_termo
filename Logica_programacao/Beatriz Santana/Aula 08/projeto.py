# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado 
# As entrada deverão ser registradas por placa. 

# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

# Passo 2:
# Verificar tempo de permanencia
# Valor a ser cobrado

# Passo 3:
# Saida como sera?
# Calcular tempo de permanencia
# Se for tag gerar na fatura da tag
# Pagar ticket
# Devolver ticket na saida

# Passo 4:
# Gerar relatorio de entradas e saidas
# Tratamento de Erros
# Revisão do código

tag_ticket = print(input(f"Olá você usará a {"Tag"} ou o {"Ticket"} ?: "))
placa = input(f"Qual é a placa do carro?: ")
entrada = input(f"Qual foi o horário de entrada do veículo?: ")
if "Tag" in tag_ticket:
    dados_tag = placa + entrada
    print(f"Aguarde o levantamento da catraca")
elif "Ticket" in tag_ticket:
    print(f"Aperte o botão para retirada do ticket e Aguarde o levantamento da catraca")
    dados_ticket = placa + entrada
    



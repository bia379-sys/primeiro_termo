def saudacao(nome):
    return f"olá, {nome}!"

# mensagem = saudacao("Beatriz")
# print(mensagem)
# Funções são blocos de código reutilizáveis.
# O "f" no Python, usado antes das aspas de uma string (como f "texto{variável}"), indica que se trata de uma f-string (ou formatted string literal). Ele informa ao Python que a string contém expressões entre chaves {} que devem ser avaliadas em tempo de execução e substituídas pelos seus valores reais. 

def age(idade):
    return f"Sua idade é {idade}!"
mensagem = age(16)
print(mensagem)

def boas_vindas(nome, cargo):
    print(f"Olá, {nome}! Você é o novo {cargo}.")
boas_vindas("Nathaniel , empresario")
boas_vindas("Sienna , artista")
boas_vindas("Anthony , desenvolvedor")

# Conversões
nome = input("Seu nome: ")
idade = int(input("Sua idade: ")) #Converte texto inteiro
print(f"{nome} tem {idade} anos.")
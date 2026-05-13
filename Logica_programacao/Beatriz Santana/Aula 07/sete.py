# Clean Code - Aula 7
# Para que usar?
# Como usar?
#print("Clean Code - Aula 7")
#aula = 7
#print(f"Estamos na aula {aula} de Clean Code")

#nome_usuario = input("Qual é o seu nome de usuário?: \n")
#nivel_usuario = int(input("Em qual nível você está?: \n"))
#print(input(f"O jogador {nome_usuario} está no nível {nivel_usuario} e pronto para a partida!"))

#2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e multiplique por 4 para mostrar quanto ele terá no final do mês.
#mesada_semana = float(input("Quanto você ganha por semana?: "))
#mesada_total = mesada_semana*4
#print(float(input(f"O total de dinheiro que você terá no final do mês será de {mesada_total}")))

# # Manipulação de arquivos e texto
# manipular_texto =" Python é Muito legal! "
# print(manipular_texto.strip().upper()) # "PYTHON"
# print(manipular_texto.strip().lower()) # "pyhton"
# print(manipular_texto.strip().startwith("A")) #"Começar com letra inicial"
# print(manipular_texto.strip().capitalize()) #"Letras Iniciais maiúscula"
# print(manipular_texto.strip().title()) # "Titulo"
# print(manipular_texto.strip().replace(" "," ")) # "Preencher vazios"
# print(manipular_texto.strip().split()) # "Separar palavras"

# # Exercício 1:
# # Crie um programa que peça ao usuário para inserir uma frase e, em seguida exiba a frase com as seguintes transformações:
# # - Deixe o texto em letras minúsculas
# frase_usuario = (input("Digite uma frase: "))
# print(frase_usuario.strip().lower())

# Manipular arquivos:
# Escrevendo
# with open("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Palmeiras é líder!")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estou evoluindo.")

# # Lendo
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo.
# Exiba o resultado para o usuário.
# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON")
#     contagem = conteudo.lower().count("python")
#     print(f"A contagem de palavras é de...{contagem}")

# Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# Criar pastas
#os.mkdir("Beah")
# Criar arquivos

# Renomear pastas
#os.rename("Beah", "Minha_Pasta")

# Apagar pastas
#os.rmdir("Minha_Pasta")
os.remove("Beah") #Excluir arquivos
import tkinter as tk
from tkinter import messagebox, ttk


def bemvindo(): 
    #.get() Serve para buscar o texto da caixa 
    nome_usuario = usuario_nome.get()
    titulo_livro = livro_titulo.get()
    leitor_perfil = perfil_leitor.get()
    categoria_livro = livro_categoria.get()

    if nome_usuario == "" and titulo_livro == "" and leitor_perfil == "" and categoria_livro == "":
        messagebox.showinfo("Verificar!", "Verificar dados!")
    elif categoria_livro == "Raro" and leitor_perfil == "Comunidade Geral":
        messagebox.showinfo("Aviso", "Livros Raros não podem ser emprestados para a comunidade geral!")
    else:
        messagebox.showinfo("Concluido", "Alunos tem 14 dias de leitura gratuita", "Comunidae tem 7 dias de leitura gratuita", "Após este período taxa de R$5,00 p/dia")
    

biblioteca_bemvindo = tk.Tk()
biblioteca_bemvindo.title("Biblioteca digital")
biblioteca_bemvindo.geometry("700x700")



lbl_titulo_pagina = tk.Label(biblioteca_bemvindo, text="Bem-vindo a Biblioteca Digital" , font=("Arial", 12, "bold"))
lbl_titulo_pagina.grid(row=0,column=0, padx=10, pady=10) 

lbl_titulo_pagina2 = tk.Label(biblioteca_bemvindo, text="Dados do empréstimo" , font=("Arial", 12, "bold"))
lbl_titulo_pagina2.grid(row=1, column=0, padx=10, pady=10)


lbl_biblioteca_usuario = tk.Label(biblioteca_bemvindo, text="Digite seu nome")
lbl_biblioteca_usuario.grid(row=2, column=0, pady=10, padx=10)
lbl_biblioteca_livro = tk.Label(biblioteca_bemvindo, text="Título do livro")
lbl_biblioteca_livro.grid(row=3, column=0, pady=10, padx=10)
lbl_biblioteca_perfil = tk.Label(biblioteca_bemvindo, text="Perfil do usuário")
lbl_biblioteca_perfil.grid(row=4, column=0, pady=10, padx=10)
lbl_biblioteca_categoria = tk.Label(biblioteca_bemvindo, text="Categoria do livro")
lbl_biblioteca_categoria.grid(row=5, column=0, pady=10, padx=10)


# Entry
usuario_nome = tk.Entry(biblioteca_bemvindo, font=("Arial", 12), width=30)
usuario_nome.grid(row=2, column=1, pady=10, padx=10)

livro_titulo = tk.Entry(biblioteca_bemvindo, font=("Arial", 12), width=30)
livro_titulo.grid(row=3, column=1, pady=10, padx=10)


# Componentes de ComboBox
perfil_leitor = tk.ttk.Combobox(biblioteca_bemvindo, values=["Aluno", "Comunidade geral"], width=30)
perfil_leitor.grid(row=4, column=1, pady=10, padx=10)
livro_categoria = tk.ttk.Combobox(biblioteca_bemvindo, values=["Raro", "Comum", "Clássico", "Edição Especial"], width=30)
livro_categoria.grid(row=5, column=1, pady=10, padx=10)



# Botão 
btn_enviar_mensagem = tk.Button(biblioteca_bemvindo, text="Validar Empréstimo", command=bemvindo, bg="#158b47" , fg="light green")
btn_enviar_mensagem.grid(row=6, column=1, pady=10, padx=10)

btn_clicar_fechar = tk.Button(biblioteca_bemvindo,text="Fechar", command=biblioteca_bemvindo.destroy, bg="#015c27" , fg="light green")
btn_clicar_fechar.grid(row=6, column=0, pady=10, padx=10)




biblioteca_bemvindo.mainloop()

import tkinter as tk
from tkinter import messagebox, ttk


def bemvindo(): 
    #.get() Serve para buscar o texto da caixa 
    nome_usuario = usuario_nome.get()
    idade_usuario = usuario_idade.get()
    

    if nome_usuario == "" and idade_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite seu nome e idade :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema! sua idade é {idade_usuario}")

biblioteca_bemvindo = tk.Tk()
biblioteca_bemvindo.title("Biblioteca digital")
biblioteca_bemvindo.geometry("500x500")



lbl_titulo_pagina = tk.Label(biblioteca_bemvindo, text="Bem-vindo a Biblioteca Digital" , font=("Arial", 16, "bold"))
lbl_titulo_pagina.grid(row=0,column=0, padx=10, pady=10) 

lbl_titulo_pagina2 = tk.Label(biblioteca_bemvindo, text="Dados do empréstimo" , font=("Arial", 12, "bold"))
lbl_titulo_pagina2.grid(row=2, column=2, padx=10, pady=10)


lbl_biblioteca_usuario = tk.Label(biblioteca_bemvindo, text="Digite seu nome :)")
lbl_biblioteca_usuario.grid(row=5, column=0, pady=10, padx=10)

lbl_biblioteca_idade = tk.Label(biblioteca_bemvindo, text="Título do livro :) ")
lbl_biblioteca_idade.grid(row=6, column=0, pady=10, padx=10)

lbl_biblioteca_pais = tk.Label(biblioteca_bemvindo, text="Perfil do usuário :)")
lbl_biblioteca_pais.grid(row=7, column=0, pady=10, padx=10)



# Entrys
usuario_nome = tk.Entry(biblioteca_bemvindo, font=("Arial", 15), width=30)
usuario_nome.grid(row=0, column=1, pady=10, padx=10)

usuario_idade = tk.Entry(biblioteca_bemvindo, font=("Arial", 15), width=30)
usuario_idade.grid(row=1, column=1, pady=10, padx=10)


# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(biblioteca_bemvindo, values=["Aluno", "Comunidade geral"], width=30)
combo_nivel.grid(row=2, column=1, pady=10, padx=10)

# Botão 
btn_enviar_mensagem = tk.Button(biblioteca_bemvindo, text="Validar Empréstimo", command=bemvindo, bg="#158b47" , fg="light green")
btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)

btn_clicar_fechar = tk.Button(biblioteca_bemvindo,text="Fechar aplicativo", command=biblioteca_bemvindo.destroy, bg="#015c27" , fg="light green")
btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)




biblioteca_bemvindo.mainloop()

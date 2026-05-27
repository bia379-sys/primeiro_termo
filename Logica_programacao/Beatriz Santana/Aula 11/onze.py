# Interface Gráfica com Tkinter
# Os componentes principais (Widgets)
# Tk: Janela principal
# Label: É o texto a digitar = print
# Button: Botão é clicável de evento.
# Entry:Caixa de texto = input
  
#0. Biblioteca
import tkinter as tk
from tkinter import messagebox

#1. Criar janela
janela = tk.Tk()
janela.title("Minha Primeira Janela em GUI")
janela.geometry("800x400")

#2. Criar função do botão
def mostrar_mensagem():
    messagebox.showinfo("Sucesso", "Você clicou no botão :) ")

#3. Criar os componentes
lbl_titulo_pagina = tk.Label(janela, text="Bem-vindo a aula de Interface Gráfica em Pyhton" , font=("Arial", 14, "bold"))
lbl_titulo_pagina2 = tk.Label(janela, text="Segue o Líder!!!!!" , font=("Arial", 14, "bold"))
btn_clique_ativar = tk.Button(janela, text="Clique Aqui :) ", font=("Arial", 14), bg="#158b47" , fg="light green" , command=mostrar_mensagem)
btn_clicar_fechar = tk.Button(janela, text="Fechar aplicativo", command=janela.destroy)
lbl_titulo_pagina.grid(row=1, column=0, padx=10, pady=10) #resumo do passo 4
btn_clique_ativar.grid(row=3, column=1, padx=16, pady=16)
btn_clicar_fechar.grid(row=4, column=1, padx=15, pady=15)
lbl_titulo_pagina2.grid(row=2, column=0, padx=10, pady=10)

#4. posicionar os componentes na janela
# lbl_titulo_pagina.pack(pady=5) #adiciona espaçamento
# btn_clique_ativar.pack(pady=10)
# btn_clicar_fechar.pack(pady=15)


#5. Rodar interface
janela.mainloop()
 

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

def segunda_janela():
    segunda_janela = tk.Toplevel(janela_bemvindo)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("500x500")

    lbl_segunda_janela = tk.Label(segunda_janela, text="Bem-Vindo, SEGUE O LÍDER :)")
    lbl_segunda_janela.grid(row=0, column=0, pady=10, padx=10)


# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("Saudações do usuário")
janela_bemvindo.geometry("500x500")

# Componentes
# Labels
lbl_menssagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome :)")
lbl_menssagem_usuario.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite sua idade :)")
lbl_mensagem_idade.grid(row=1, column=0, pady=10, padx=10)

lbl_mensagem_pais = tk.Label(janela_bemvindo, text="Escolha seu país :)")
lbl_mensagem_pais.grid(row=2, column=0, pady=10, padx=10)



# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 15), width=30)
usuario_nome.grid(row=0, column=1, pady=10, padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 15), width=30)
usuario_idade.grid(row=1, column=1, pady=10, padx=10)


# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Brasil", "Marrocos", "Egito", "Escócia"], width=30)
combo_nivel.grid(row=2, column=1, pady=10, padx=10)

# Botão 
btn_enviar_mensagem = tk.Button(janela_bemvindo, text="Enviar Mensagem", command=bemvindo, bg="#158b47" , fg="light green")
btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)

btn_clicar_fechar = tk.Button(janela_bemvindo, text="Fechar aplicativo", command=janela_bemvindo.destroy, bg="#015c27" , fg="light green")
btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)

btn_segunda_janela = tk.Button(janela_bemvindo, text="Abrir Segunda Janela", command=segunda_janela, bg="#427456" , fg="light green")
btn_segunda_janela.grid(row=5, column=1, pady=10, padx=10)


# Rodar interface
janela_bemvindo.mainloop()

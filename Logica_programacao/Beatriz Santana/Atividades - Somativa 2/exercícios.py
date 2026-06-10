# # 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# # "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# import tkinter as tk
# from tkinter import messagebox, ttk

# def registro():
#     nome_operador = operador_nome.get()
#     turno_operador = operador_turno.get()

#     if nome_operador == "" and turno_operador == "":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e turno")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Olá {nome_operador}, logando no sistema! seu turno é {turno_operador}")

# janela_registro = tk.Tk()
# janela_registro.title("Registro do Operador")
# janela_registro.geometry("500x500")

# lbl_mensagem_operador = tk.Label(janela_registro, text="Digite seu nome")
# lbl_mensagem_operador.grid(row=0, column=0, pady=10, padx=10)
# lbl_mensagem_operador = tk.Label(janela_registro, text="Selecione seu turno" )
# lbl_mensagem_operador.grid(row=1, column=0, pady=10, padx=10)

# operador_nome = tk.Entry(janela_registro, font=("Arial", 15), width=30)
# operador_nome.grid(row=0, column=1, pady=10, padx=10)
# operador_turno = tk.ttk.Combobox(janela_registro, values=["A", "B", "C"], width=30)
# operador_turno.grid(row=1, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_registro, text="Enviar Registro", command=registro, bg="#000000" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_registro, text="Fechar", command=janela_registro.destroy, bg="#015c27" , fg="light green")
# btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)

# janela_registro.mainloop()


# # 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e exiba quantas peças serão produzidas em um turno de 8 horas.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def producao():
#     quantia_producao = int(producao_quantia.get())
#     if quantia_producao == "": 
#         messagebox.showwarning("Aviso", "Por favor digite os dados para o cálculo")
#     else:
#         total = quantia_producao * 8 
#         messagebox.showinfo("Total",f"A quantidade peças produzidas é de {total}")

# janela_producao = tk.Tk()
# janela_producao.title("Cálculo de produção")
# janela_producao.geometry("500x500")

# lbl_menssagem_producao= tk.Label(janela_producao, text="Quantas peças são produzidas por hora?")
# lbl_menssagem_producao.grid(row=0, column=1, pady=10, padx=10)
# producao_quantia = tk.Entry(janela_producao, font=("Arial", 15), width=30)
# producao_quantia.grid(row=1, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_producao, text="Calcular", command=producao, bg="#EB78C5" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_producao, text="Fechar", command=janela_producao.destroy, bg="#000000" , fg="light pink")
# btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)

# janela_producao.mainloop()


# # 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# # ≈ 14.5 PSI) e exiba com duas casas decimais.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def conversor():
#     conversor_unidade = float(unidade_conversor.get())
#     if conversor_unidade == "": 
#         messagebox.showwarning("Aviso", "Por favor digite os dados para o cálculo")
#     else:
#         total = conversor_unidade * 14.5 
#         messagebox.showinfo("Conversor",f"A conversão para PSI é de:{total}")

# janela_conversor = tk.Tk()
# janela_conversor.title("Conversor de unidade")
# janela_conversor.geometry("400x400")

# lbl_menssagem_conversor = tk.Label(janela_conversor, text="Qual é a pressão em Bar?")
# lbl_menssagem_conversor.grid(row=0, column=0, pady=10, padx=10)
# unidade_conversor = tk.Entry(janela_conversor, font=("Arial", 15), width=30)
# unidade_conversor.grid(row=1, column=0, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_conversor, text="Calcular", command=conversor, bg="#EB78C5" , fg="black")
# btn_enviar_mensagem.grid(row=2, column=0, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_conversor, text="Fechar", command=janela_conversor.destroy, bg="#000000" , fg="light pink")
# btn_clicar_fechar.grid(row=3, column=0, pady=10, padx=10)

# janela_conversor.mainloop()


# # 5. Termostato Inteligente: Peça a temperatura de um motor.
# # ● Abaixo de 40°C: "Baixa carga".
# # ● Entre 40°C e 70°C: "Normal".
# # ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# import tkinter as tk
# from tkinter import messagebox, ttk
# def termostato():
#     temperatura_motor = motor_temperatura.get()
    
#     if temperatura_motor <= "40":
#         messagebox.showwarning("Aviso", "Baixa Carga!")
#     elif temperatura_motor >= "70":
#         messagebox.showwarning("Aviso", "ALERTA: Resfriamento ativado!")
#     else:
#         messagebox.showwarning("Aviso", "Temperatura Normal")

# janela_termostato = tk.Tk()
# janela_termostato.title("Termostato Inteligente")
# janela_termostato.geometry("500x500")

# lbl_menssagem_temperatura = tk.Label(janela_termostato, text="Digite a temperatura do motor")
# lbl_menssagem_temperatura.grid(row=0, column=0, pady=10, padx=10)
# motor_temperatura = tk.Entry(janela_termostato, font=("Arial", 15), width=30)
# motor_temperatura.grid(row=1, column=0, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_termostato, text="Enviar Mensagem", command=termostato , bg="#fbff1f" , fg="black")
# btn_enviar_mensagem.grid(row=2, column=0, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_termostato, text="Fechar", command=janela_termostato.destroy, bg="#e8f3a9" , fg="black")
# btn_clicar_fechar.grid(row=2, column=1, pady=10, padx=10)

# janela_termostato.mainloop()


# # 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# # exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".
# import tkinter as tk
# from tkinter import messagebox, ttk
# def lotes():
#     classificar_lotes = lotes_classificar.get()
#     if classificar_lotes == "A":
#         messagebox.showwarning("Classificação", "Alimentos")
#     elif classificar_lotes == "E":
#         messagebox.showwarning("Classificação", "Eletrônicos")
#     else:
#         messagebox.showinfo("Classificação", "Desconhecido")

# janela_lotes = tk.Tk()
# janela_lotes.title("Classificador de Lotes")
# janela_lotes.geometry("500x500")

# lbl_menssagem_lote = tk.Label(janela_lotes, text="Digte a primeira letra do código do produto")
# lbl_menssagem_lote.grid(row=0, column=0, pady=10, padx=10)
# lotes_classificar = tk.Entry(janela_lotes, font=("Arial", 15), width=30)
# lotes_classificar.grid(row=1, column=0, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_lotes, text="Verificar", command=lotes, bg="#fbff1f" , fg="black")
# btn_enviar_mensagem.grid(row=2, column=0, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_lotes, text="Fechar", command=janela_lotes.destroy, bg="#e8f3a9" , fg="black")
# btn_clicar_fechar.grid(row=2, column=1, pady=10, padx=10)

# janela_lotes.mainloop()



# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.
import tkinter as tk
from tkinter import messagebox, ttk
def seguranca():
    sensor_porta = porta_sensor.get()
    botao_emergencia = emergencia_botao.get()
    if sensor_porta == "Fechada" and botao_emergencia == "Desligado":
        messagebox.showwarning("Operação", "A máquina pode iniciar!")
    else:
        messagebox.showwarning("Operação", "A máquina não pode ser iniciada, verifique os sensores" )

janela_seguranca = tk.Tk()
janela_seguranca.title("Segurança da operação")
janela_seguranca.geometry("500x500")

lbl_menssagem_sensor = tk.Label(janela_seguranca, text="Qual é o estado da porta?")
lbl_menssagem_sensor.grid(row=0, column=0, pady=10, padx=10)
lbl_menssagem_botao = tk.Label(janela_seguranca, text="Qual é o estado do botão de emergência?")
lbl_menssagem_botao.grid(row=1, column=0, pady=10, padx=10)

porta_sensor = tk.ttk.Combobox(janela_seguranca, values=["Fechada", "Aberta"], width=30)
porta_sensor.grid(row=0, column=1, pady=10, padx=10)
emergencia_botao = tk.ttk.Combobox(janela_seguranca, values=["Desligado", "Ligado"], width=30)
emergencia_botao.grid(row=1, column=1, pady=10, padx=10)

btn_enviar_mensagem = tk.Button(janela_seguranca, text="Analisar", command=seguranca, bg="#158b47" , fg="light green")
btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)

btn_clicar_fechar = tk.Button(janela_seguranca, text="Fechar", command=janela_seguranca.destroy, bg="#015c27" , fg="light green")
btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)


janela_seguranca.mainloop()
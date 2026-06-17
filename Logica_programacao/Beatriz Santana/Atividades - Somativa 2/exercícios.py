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


# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def qualidade():
#     peca_um = int(um_peca.get())
#     peca_dois = int(dois_peca.get())
#     peca_tres = int(tres_peca.get())

#     if peca_um == "" and peca_dois == "" and peca_tres == "":
#         messagebox.showwarning("Aviso", "Insira as notas de inspeção")

#     else:
#         media = 3 / peca_um + peca_dois + peca_tres
#         messagebox.showinfo("Aviso", f"A média de qualidade das peças é {media}")

# janela_qualidade = tk.Tk()
# janela_qualidade.title("Média de Qualidade")
# janela_qualidade.geometry("500x500")

# lbl_menssagem_tit = tk.Label(janela_qualidade, text="Média de qualidade")
# lbl_menssagem_tit.grid(row=0, column=0, pady=10, padx=10)
# lbl_menssagem_um = tk.Label(janela_qualidade, text="Qual é a nota da peça 1?")
# lbl_menssagem_um.grid(row=1, column=0, pady=10, padx=10)
# lbl_menssagem_dois = tk.Label(janela_qualidade, text="Qual é a nota da peça 2?")
# lbl_menssagem_dois.grid(row=2, column=0, pady=10, padx=10)
# lbl_menssagem_tres = tk.Label(janela_qualidade, text="Qual é a nota da peça 3?")
# lbl_menssagem_tres.grid(row=3, column=0, pady=10, padx=10)

# um_peca = tk.ttk.Combobox(janela_qualidade, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], width=30)
# um_peca.grid(row=1, column=1, pady=10, padx=10)
# dois_peca = tk.ttk.Combobox(janela_qualidade, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], width=30)
# dois_peca.grid(row=2, column=1, pady=10, padx=10)
# tres_peca = tk.ttk.Combobox(janela_qualidade, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], width=30)
# tres_peca.grid(row=3, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_qualidade, text="Calcular", command=qualidade, bg="#158b47" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_qualidade, text="Fechar", command=janela_qualidade.destroy, bg="#015c27" , fg="light green")
# btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)

janela_qualidade.mainloop()

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



# # 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# # botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# # iniciar.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def seguranca():
#     sensor_porta = porta_sensor.get()
#     botao_emergencia = emergencia_botao.get()
#     if sensor_porta == "Fechada" and botao_emergencia == "Desligado":
#         messagebox.showwarning("Operação", "A máquina pode iniciar!")
#     else:
#         messagebox.showwarning("Operação", "A máquina não pode ser iniciada, verifique os sensores" )

# janela_seguranca = tk.Tk()
# janela_seguranca.title("Segurança da operação")
# janela_seguranca.geometry("500x500")

# lbl_menssagem_sensor = tk.Label(janela_seguranca, text="Qual é o estado da porta?")
# lbl_menssagem_sensor.grid(row=0, column=0, pady=10, padx=10)
# lbl_menssagem_botao = tk.Label(janela_seguranca, text="Qual é o estado do botão de emergência?")
# lbl_menssagem_botao.grid(row=1, column=0, pady=10, padx=10)

# porta_sensor = tk.ttk.Combobox(janela_seguranca, values=["Fechada", "Aberta"], width=30)
# porta_sensor.grid(row=0, column=1, pady=10, padx=10)
# emergencia_botao = tk.ttk.Combobox(janela_seguranca, values=["Desligado", "Ligado"], width=30)
# emergencia_botao.grid(row=1, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_seguranca, text="Analisar", command=seguranca, bg="#158b47" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)

# btn_clicar_fechar = tk.Button(janela_seguranca, text="Fechar", command=janela_seguranca.destroy, bg="#015c27" , fg="light green")
# btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)


# janela_seguranca.mainloop()


# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".
# import tkinter as tk
# from tkinter import messagebox, ttk
# def descarte():
#     pecas_produzidas = float(produzidas_pecas.get())
#     descarte_defeituosas = float(defeituosas_descarte.get())

#     if descarte_defeituosas >= pecas_produzidas:
#         messagebox.showwarning("Aviso", "Revisar Processo!")
#     else:
#         messagebox.showinfo("Aviso", "Processo Otimizado")

# janela_descarte = tk.Tk()
# janela_descarte.title("Cálculo de Descarte")
# janela_descarte.geometry("500x500")

# lbl_menssagem_inicial = tk.Label(janela_descarte, text="Cálculo de Descarte")
# lbl_menssagem_inicial.grid(row=0, column=1, pady=10, padx=10)
# lbl_menssagem_pecas = tk.Label(janela_descarte, text="Total de peças produzidas")
# lbl_menssagem_pecas.grid(row=1, column=0, pady=10, padx=10)
# lbl_mensagem_defeituosas = tk.Label(janela_descarte, text="Total de peças defeituosas")
# lbl_mensagem_defeituosas.grid(row=2, column=0, pady=10, padx=10)


# produzidas_pecas = tk.Entry(janela_descarte, font=("Arial", 15), width=30)
# produzidas_pecas.grid(row=1, column=1, pady=10, padx=10)
# defeituosas_descarte = tk.Entry(janela_descarte, font=("Arial", 15), width=30)
# defeituosas_descarte.grid(row=2, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_descarte, text="Calcular", command=descarte, bg="#158b47" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_descarte, text="Fechar", command=janela_descarte.destroy, bg="#015c27" , fg="light green")
# btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)


# janela_descarte.mainloop()



# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.
# import tkinter as tk
# from tkinter import messagebox, ttk
# def medida():
#     validar_medida = float(medida_validar.get())

#     if validar_medida <= 9.8:
#         messagebox.showwarning("Aviso", "Medida abaixo do esperado")
#     elif validar_medida >= 10.2:
#         messagebox.showwarning("Aviso", "Medida acima do esperado")
#     else:
#         messagebox.showwarning("Aviso", "Medida dentro do tolerado")

# janela_medida = tk.Tk()
# janela_medida.title("Validação de Medida")
# janela_medida.geometry("500x500")

# lbl_menssagem_validar = tk.Label(janela_medida, text="Validação de Medida")
# lbl_menssagem_validar.grid(row=0, column=0, pady=10, padx=10)
# lbl_menssagem_validar = tk.Label(janela_medida, text="Qual é a medida da peça? ")
# lbl_menssagem_validar.grid(row=1, column=0, pady=10, padx=10)
# medida_validar = tk.Entry(janela_medida, font=("Arial", 15), width=30)
# medida_validar.grid(row=1, column=1, pady=10, padx=10)

# btn_enviar_mensagem = tk.Button(janela_medida, text="Verificar", command=medida, bg="#158b47" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=10)
# btn_clicar_fechar = tk.Button(janela_medida, text="Fechar", command=janela_medida.destroy, bg="#015c27" , fg="light green")
# btn_clicar_fechar.grid(row=4, column=0, pady=10, padx=10)

# janela_medida.mainloop()


# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".
# import tkinter as tk
# from tkinter import messagebox, ttk
# def contagem():
#     contagem_regressiva = regressiva_contagem.get()
#     if contagem_regressiva == "Sim":
#        for i in range(11):
#         print(i)
#         messagebox.showwarning("Aviso", f"Contagem regressiva ativando prensa! {i}")
#     else:
#         messagebox.showinfo("Aviso", "Não é possível iniciar contagem")


# janela_contagem = tk.Tk()
# janela_contagem.title("Saudações do usuário")
# janela_contagem.geometry("500x500")

# lbl_menssagem_usuario = tk.Label(janela_contagem, text="Contagem Regressiva de Setup")
# lbl_menssagem_usuario.grid(row=0, column=0, pady=10, padx=10)
# lbl_menssagem_usuario = tk.Label(janela_contagem, text="Quer iniciar a contagem regressiva?")
# lbl_menssagem_usuario.grid(row=2, column=0, pady=10, padx=10)
# btn_enviar_mensagem = tk.Button(janela_contagem, text="Começar Contagem", command=contagem, bg="#158b47" , fg="light green")
# btn_enviar_mensagem.grid(row=4, column=1, pady=10, padx=1)
# regressiva_contagem = tk.ttk.Combobox(janela_contagem, values=["Não", "Sim"], width=30)
# regressiva_contagem.grid(row=2, column=1, pady=10, padx=10)

# janela_contagem.mainloop()

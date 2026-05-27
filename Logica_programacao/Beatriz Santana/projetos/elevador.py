# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar
# rodando até que o usuário decida encerrar.
# alerta de excesso de peso (acima de 5 pessoas)
# 10 andares (terreo e 9 acima)
# mensagem de movimento
# loop até a parada ser solicitada

andar_atual = 0
while True:
    try:
        import time
        andar_apartamento = int(input(f"Olá, para qual andar deseja ir?(0-10): "))
        quantidade_pessoas = int(input(f"Quantas pessoas estão no elevador?: "))

        if quantidade_pessoas < 5:
            for andar_atual in range (andar_apartamento):
                print(f"Elevador em movimento {andar_atual + 1}")
                time.sleep(2)
            print("Parando...", f"Você chegou ao andar {andar_apartamento}")
            for listagem in range(10):
                print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'}")
            if input("Deseja escolher outro andar? (s/n): ").lower() != 's':
                print("Obrigado por usar o Elevador Python! Até a próxima!")
                break
        else:
            print(f"Perigo! Quantidade máxima de pessoas atingida!")
    except ValueError:
        print("Digite apenas algarismos")

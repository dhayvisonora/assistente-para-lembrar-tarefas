#VARIAVEIS
lista_das_tarefas = {"LISTA DIARIA":["planilha de pagamento", "planilha de reposição", "cancelamento de estorno", "conferência de extrato"], "LISTA DE TAREFA": []}
encerrar = True
#FUNÇÕES DE OPÇOES
def lembrete_diario():
    print("" \
    "================\n" \
    "LEMBRETE DIÁRIO\n" \
    "================\n" \
    "Trazendo tudo da sua lista: \n" \
    "")

    for lista in range(len(lista_das_tarefas["LISTA DIARIA"])):
        print(lista + 1 , lista_das_tarefas["LISTA DIARIA"][lista])

def adicionar_tarefa():
    item = input("" \
    ">> ESCREVA QUAL A TAREFA QUE SERÁ ADICIONADA <<\n" \
    "").strip().lower()

    lista_das_tarefas["LISTA DE TAREFA"].append(item)

def visualizar_lista_de_tarefa():
    print("" \
    "=================\n" \
    "LISTA DE TAREFAS\n" \
    "=================\n" \
    "" )

    for indice in range(len(lista_das_tarefas["LISTA DE TAREFA"])):
        print(indice + 1 , lista_das_tarefas["LISTA DE TAREFA"][indice])

def remover_tarefa():
    print(""
    "===============\n"
    "REMOVER TAREFA\n"
    "===============\n")

    for indice in range(len(lista_das_tarefas["LISTA DE TAREFA"])):
        print(indice + 1 , lista_das_tarefas["LISTA DE TAREFA"][indice])
    retirar = int(input("" \
    ">>  QUAL TAREFA DESEJA REMOVER  <<\n>> "))
    retirar = retirar - 1
    del lista_das_tarefas["LISTA DE TAREFA"][retirar]

    print(""
    ">LISTA ATUALIZADA<\n"
    "")

    for indice in range(len(lista_das_tarefas["LISTA DE TAREFA"])):
        print(indice + 1 , lista_das_tarefas["LISTA DE TAREFA"][indice])

#TELA INICIAL
while encerrar:
    print("" \
    "==========================================\n" \
    "<< OLÁ, EU SOU A SUA ASSISTENTE VIRTUAL >>\n" \
    "==========================================\n" \
    "")
    resposta = int(input("" \
    "<< PARA COMEÇARMOS, DIGITE O NUMERO DA AÇÃO QUE VOCÊ DESEJA PROSSEGUIR ! >>\n" \
    "  1- Lembrete diário.\n" \
    "  2- Adicionar tarefa.\n" \
    "  3- Visualizar lista de tarefas.\n" \
    "  4- Remover tarefa.\n" \
    "  5- Encerrar programa.\n>> " \
    ""))
    if resposta == 5:
        print("" \
        "===================\n" \
        "ENCERRANDO PROGRAMA\n" \
        "===================\n")

        encerrar = False

    elif resposta == 1:
        lembrete_diario()
    elif resposta == 2:
        adicionar_tarefa()
    elif resposta == 4:
        remover_tarefa()
    elif resposta == 3:
        visualizar_lista_de_tarefa()
    else:
        print(">> DIGITE ALGUM NUMERO DAS OPÇOES ACIMA <<")
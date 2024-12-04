tarefas = []

def listar_tarefa():
    if not tarefas:
        print("Nenhuma tarefa registrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"\n{i + 1}. {tarefa['nome']} - {status} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']}")

def adicionar_tarefa():
    nome = input("\nDigite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade (Baixa, Média, Alta): ")
    categoria = input("Digite a categoria (Exemplo: Trabalho, Pessoal): ")
    
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso!")

def marcar_tarefa_concluida():
    listar_tarefa()
    
    entrada = input("\nDigite o número da tarefa que deseja marcar como concluída: ")
    
    if entrada.isdigit():
        indice = int(entrada) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]['concluida'] = True
            print("\nTarefa marcada como concluída.")
        else:
            print("\nÍndice inválido.")
    else:
        print("\nPor favor, digite um número válido.")

def menu_programa():

    while True:
        print("\nSelecione a operação:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefa")
        print("3. Marcar Tarefa Como Concluida")
        print("4. Sair")

        escolha = input("Escolha uma operação (1/2/3/4): ")
        if escolha == '4':
            print('Encerrando o programa')
            break
        elif escolha == '1':
                adicionar_tarefa()
        elif escolha == '2':
                listar_tarefa()
        elif escolha == '3':
                marcar_tarefa_concluida()
        else:
             print('[ERRO] Opção Inválida')

menu_programa()
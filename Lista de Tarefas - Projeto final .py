def adicionar_tarefa (lista_de_tarefas , tarefa):
    """Adiciona nova tarefa a uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print ('\033[1;32mTarefa Adicionada com sucesso!\033[m')
    return lista_de_tarefas

def listar_tarefas (lista_de_tarefas):
    """Exibe Lista de tarefas numeradas"""
    print ('=-=' *10)
    print ('\033[1;32mLista de Tarefas\033[m')
    print ('=-='*10)
    n = 1
    for tarefa in lista_de_tarefas:
        print (f'\033[4;36m{n} - {tarefa}\033[m')
        n = n+1
    print ('=-='*10)

def deletar_tarefa (lista_de_tarefas , tarefa):
    """Deleta tarefa de uma lista pré-existente, a partir do número dela."""
    indice = tarefa -1
    if 0<=indice<len (lista_de_tarefas):
        lista_de_tarefas.pop(indice)
    return lista_de_tarefas

def exibir_menu ( ):
    """Exibe menu com opções para usuário escolher"""
    print ('\033[4;36mEscolha uma opção:\033[m \n'
           '1 - Inserir nova tarefa \n'
           '2 - Listar tarefas \n'
           '3 - Deletar tarefa\n'
           '4 - Sair')
    print('=-=' * 10)

# Inicialização de Variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do Programa
print ('\033[1;34mBem-Vindo a sua Lista de Tarefas!\033[m')
print ('=-='*10)

# Loop principal
while continuar:
    exibir_menu()
    opcao = input ('Insira o que deseja fazer: ')
    print ('=-='*10)

    if opcao == '1':
        tarefa = input ('\033[4mInsira uma nova tarefa: \033[m')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas,tarefa)

    elif opcao == '2':
        listar_tarefas(lista_de_tarefas)

    elif opcao == '3':
        # A Validação verifica se o valor está dentro do escopo do limite da lista.
        # Prevê também se o usuário por ventura acabar digitando qualquer valor que não seja numérico,
        # evitando assim um erro e a quebra do programa
        try:
            tarefa = int(input('\033[4mInsira o numero da tarefa que deseja deletar:\033[m '))
            if 1 <= tarefa <= len(lista_de_tarefas):
                deletar_tarefa(lista_de_tarefas, tarefa)
                print('\033[1;32mTarefa deletada com sucesso!\033[m')
            else:
                print('\033[1;31mNúmero Inválido! Tente novamente.\033[m')
        except ValueError:
            print('\033[1;31mValor inválido! Por favor, digite um número.\033[m')

    elif opcao == '4':
        continuar = False
        print ('\033[1;34mSaindo, até logo!\033[m')
    else:
        print ('\033[1;31mOpção invalida! Por favor, tente novamente.\033[m')
    print ('\n')


import os

class Node:
    def __init__(self, tarefa, concluida=False, prioridade=0):
        self.tarefa = tarefa
        self.concluida = concluida
        self.prioridade = prioridade
        self.proximo = None

class ListaLanche:
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def adicionar_lanche(self, tarefa, prioridade=0):
        novo_node = Node(tarefa, prioridade=prioridade)
        if self.primeiro is None:
            self.primeiro = novo_node
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_node

    def adicionar_lanche_com_prioridade(self, tarefa, prioridade):
        novo_node = Node(tarefa, prioridade=prioridade)
        if self.primeiro is None:
            self.primeiro = novo_node
        elif self.primeiro.prioridade < prioridade:
            novo_node.proximo = self.primeiro
            self.primeiro = novo_node
        else:
            atual = self.primeiro
            while atual.proximo is not None and atual.proximo.prioridade >= prioridade:
                atual = atual.proximo
            novo_node.proximo = atual.proximo
            atual.proximo = novo_node

    def remover_lanche(self, tarefa):
        if self.primeiro is None:
            raise IndexError('The range out of list.')
        
        if self.primeiro.tarefa == tarefa:
            self.primeiro = self.primeiro.proximo
            return True

        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.tarefa == tarefa:
                atual.proximo = atual.proximo.proximo
                return True
            atual = atual.proximo
        raise ValueError("Task not found")

    def marcar_como_feito(self, tarefa):
        atual = self.primeiro
        while atual is not None:
            if atual.tarefa == tarefa:
                atual.concluida = True
                return
            atual = atual.proximo
        raise ValueError("Task not found")

    def marcar_como_nao_feito(self, tarefa):
        atual = self.primeiro
        while atual is not None:
            if atual.tarefa == tarefa:
                atual.concluida = False
                return
            atual = atual.proximo
        raise ValueError("Task not found")

    def ordenar_lanches_por_prioridade(self):
        # Obter uma lista de tuplas (prioridade, tarefa) de todos os elementos da lista
        tarefas = [(nodo.tarefa, nodo.concluida, nodo.prioridade) for nodo in self.__iter__()]

        # Ordenar a lista de tuplas pela prioridade em ordem decrescente
        tarefas = sorted(tarefas, key=lambda tup: tup[2], reverse=True)

        # Recriar a lista encadeada com as tarefas na nova ordem
        self.primeiro = None
        for tarefa, concluida, prioridade in tarefas:
            novo_node = Node(tarefa, concluida=concluida, prioridade=prioridade)
            novo_node.proximo = self.primeiro
            self.primeiro = novo_node
    
    def listar_lanches(self):
        if self.primeiro is None:
            print('A lista está vazia.')
        else:
            print('Lanches:')
            atual = self.primeiro
            while atual is not None:
                concluida = 'concluído' if atual.concluida else 'não concluído'
                print(f'{atual.tarefa} - {concluida} - Prioridade: {atual.prioridade}')
                atual = atual.proximo


lista_lanche = ListaLanche()

while True: 
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal
    print('1 - Criar lista encadeada')
    print('2 - Adicionar lanche')
    print('3 - Remover lanche')
    print('4 - Marcar como concluído')
    print('5 - Marcar como não concluído')
    print('6 - Ordenar lanches por prioridade')
    print('7 - Listar lanches')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Lista encadeada criada.')
    elif opcao == '2':
        tarefa = input('Digite o nome do lanche: ')
        prioridade = int(input('Digite a prioridade da tarefa: '))
        lista_lanche.adicionar_lanche_com_prioridade(tarefa, prioridade=prioridade)
    elif opcao == '3':
        tarefa = input('Digite o nome do lanche a ser removido: ')
        lista_lanche.remover_lanche(tarefa)
    elif opcao == '4':
        tarefa = input('Digite o nome do lanche a ser marcado como concluído: ')
        lista_lanche.marcar_como_feito(tarefa)
    elif opcao == '5':
        tarefa = input('Digite o nome do lanche a ser marcado como não concluído: ')
        lista_lanche.marcar_como_nao_feito(tarefa)
    elif opcao == '6':
        lista_lanche.ordenar_lanches_por_prioridade()
    elif opcao == '7':
        lista_lanche.listar_lanches()
    elif opcao == '0':
        break
    else:
        print('Opção inválida. Tente novamente.')
        continue

    input('Pressione Enter para continuar...')

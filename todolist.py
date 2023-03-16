import os

class Node:
    def __init__(self, tarefa, concluida=False):
        self.tarefa = tarefa
        self.concluida = concluida
        self.proximo = None


class ListaLanche:
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def adicionar_lanche(self, tarefa):
        novo_node = Node(tarefa)
        if self.primeiro is None:
            self.primeiro = novo_node
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_node

    def remover_lanche(self, tarefa):
        if self.primeiro is None:
            return IndexError('The range out of list.')
        
        if self.primeiro.tarefa == tarefa:
            self.primeiro = self.primeiro.proximo
            return True

        atual = self.primeiro
        while atual.proximo is not None:
            if atual.proximo.tarefa == tarefa:
                atual.proximo = atual.proximo.proximo
                return True
            atual = atual.proximo

    def marcar_como_feito(self, tarefa):
        atual = self.primeiro
        while atual is not None:
            if atual.tarefa == tarefa:
                atual.concluida = True
                return
            atual = atual.proximo

    def marcar_como_nao_feito(self, tarefa):
        atual = self.primeiro
        while atual is not None:
            if atual.tarefa == tarefa:
                atual.concluida = False
                return
            atual = atual.proximo

    def listar_lanches(self):
        atual = self.primeiro
        while atual is not None:
            status = 'Concluída' if atual.concluida else 'Não concluída'
            print(f'{atual.tarefa} ({status})')
            atual = atual.proximo




lista_lanche = ListaLanche()

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal
    print('1 - Criar lista encadeada')
    print('2 - Adicionar lanche')
    print('3 - Remover lanche')
    print('4 - Marcar como concluído')
    print('5 - Marcar como não concluído')
    print('6 - Listar lanches')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Lista encadeada criada.')
    elif opcao == '2':
        tarefa = input('Digite o nome do lanche: ')
        lista_lanche.adicionar_lanche(tarefa)
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
        lista_lanche.listar_lanches()
    elif opcao == '0':
        break
    else:
        print('Opção inválida. Tente novamente.')
        continue
    
    input('Pressione Enter para continuar...')

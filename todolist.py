class Node:
    def __init__(self, tarefa, concluida = False):
        self.tarefa = tarefa
        self.concluida = concluida
        self.proximo = None

class ListaTarefas:
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    def adicionar_tarefas(self,tarefa):
        novo_node = Node(tarefa)
        if self.primeiro is None:
            self.primeiro = novo_node
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual = novo_node

    def remover_tarefa(self, tarefa):
        if self.primeiro is None:
            return
        if self.primeiro.tarefa == tarefa:
            self.primeiro = self.primeiro.proximo
            return
    
        atual = self.primeiro
        while atual.proximo is not None:
            atual.proximo = atual.proximo.proximo
            return
        atual = atual.proximo
    
    def marcar_como_concluida(self,tarefa):
        atual = self.primeiro
        while atual is not None:
            if atual.tarefa == tarefa:
                atual.concluida = True
                return
            atual = atual.proximo
        
    def marcar_como_nao_concluida(self, tarefa):
        atual = self.primeiro
        while atual is not None:
            status = 'Concluida.' if atual.concluida else 'Não concluída.'
            print(f'{atual.tarefa} ({status})')
            atual = atual.proximo

lista = ListaTarefas()

lista.adicionar_tarefa("Fazer compras")
lista.adicionar_tarefa("Lavar roupa")
lista.adicionar_tarefa("Estudar Python")

lista.listar_tarefa()
# Saída: 
# Fazer compras (Não Concluída)
# Lavar roupa (Não Concluída)
# Estudar Python (Não Concluída)

lista.marcar_como_concluida("Fazer compras")
lista.marcar_como_concluida("Lavar roupa")

lista.listar_tarefas()
# Saída:
# Fazer compras (Concluída)
# Lavar roupa (Concluída)
# Estudar Python (Não Concluída)

lista.remover_tarefa("Lavar roupa")

lista.listar_tarefas()
# Saída:
# Fazer compras (Concluída)
# Estudar Python (Não Concluída)
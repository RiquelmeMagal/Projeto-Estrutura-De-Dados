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


lista = ListaLanche()

lista.adicionar_lanche("1 coxinha")
lista.adicionar_lanche("2 pasteis")
lista.adicionar_lanche("1 pizza")
lista.adicionar_lanche('1 arroz e feijao')
print('-'*10)
lista.listar_lanches()
#

print('-'*10)
lista.marcar_como_feito("1 coxinha")
lista.marcar_como_feito("2 pasteis")

lista.listar_lanches()
#

lista.remover_lanche("1 arroz e feijao")
print('-'*10)
lista.listar_lanches()
# 

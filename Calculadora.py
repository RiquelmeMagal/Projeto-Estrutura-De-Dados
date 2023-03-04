class Calculadora:
    def __init__(self):
        self.items = []

    def empilhar(self,item):
        self.items.append(item)

    def desempilhar(self,item):
        return self.items.pop()
    
    def topo(self):
        return self.items[-1]
    
    
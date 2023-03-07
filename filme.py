class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.proximo = None

def adicionarFilme(inicio):
    titulo = input("Digite o titulo do filme: ")
    diretor = input("Digite o diretor do filme: ")
    ano = input("Digite o ano de lancamento do filme: ")

    novoFilme = Filme(titulo, diretor, ano)
    novoFilme.proximo = inicio
    inicio = novoFilme
    return inicio

def buscarFilme(inicio, titulo):
    atual = inicio
    while atual is not None:
        if atual.titulo == titulo:
            print("Titulo:", atual.titulo)
            print("Diretor:", atual.diretor)
            print("Ano de lancamento:", atual.ano)
            return
        atual = atual.proximo
    print("Filme nao encontrado.")

def listarFilmes(inicio):
    if inicio is None:
        print("A lista esta vazia.")
        return

    atual = inicio
    while atual is not None:
        print("Titulo:", atual.titulo)
        print("Diretor:", atual.diretor)
        print("Ano de lancamento:", atual.ano)
        print()
        atual = atual.proximo

def main():
    listaDeFilmes = None
    opcao = 0

    while opcao != 4:
        print("Catalogo de filmes")
        print("1. Adicionar filme")
        print("2. Buscar filme")
        print("3. Listar filmes")
        print("4. Sair")
        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            listaDeFilmes = adicionarFilme(listaDeFilmes)
        elif opcao == 2:
            titulo = input("Digite o titulo do filme que deseja buscar: ")
            buscarFilme(listaDeFilmes, titulo)
        elif opcao == 3:
            listarFilmes(listaDeFilmes)
        elif opcao == 4:
            print("Saindo do programa.")
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    main()

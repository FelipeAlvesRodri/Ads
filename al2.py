qtde_livros = int(input("quantos livros comprados: "))
clube = int(input("Participa do clube?: 0-NÃO,1-Sim "))
soma_livros = 0

for i in range(qtde_livros):
    valor_livros = float(input("Qual o valor do livro: "))
    soma_livros = soma_livros + valor_livros

print(soma_livros)
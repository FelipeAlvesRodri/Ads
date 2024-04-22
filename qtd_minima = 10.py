qtd_minima = 10
qtd_produto = int(input("Quantidade do produto: "))

if qtd_produto > qtd_minima:
    print("Produto disponivel em estoque. Aproveite!")
else:
    print("Produto indisponivel no estoque. Volte mais tarde!")
    

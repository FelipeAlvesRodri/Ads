livro = int(input("Quantos livros irá comprar? "))
preço = float(input("Qual o preço de cada livro? "))
if livro == 1:
    print(f"Nao terá desconto, total: R${preço} ")

elif livro >= 2:
    preço = livro*preço
    total = preço*0.9
    print(f"Terá desconto de 10% sobre o valor total: R${total}")

elif livro >= 4: 
    preço = livros*preço
    total = preço*0.8
    print(f"Terá desconto de 20% sobre o valor total : R${total}")

else: 
   preço = livros*preço
   total = preço*0,7
   print(f"Terá desconto de 30% sobre o valor total : R${total}")



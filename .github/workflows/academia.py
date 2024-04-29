port = input("Tem um portifolio forte? ")
audi =  input("Sua audição foi exelente? ")
previo =  int(input("Quantos anos de treinamento previo vc tem? "))

if port =='sim' or port == 'tenho':
    port = True
else: 
    port = False

if audi =='sim':
    audi = True
else: 
    audi = False

if port or audi and previo >= 2:
    print("Vc será admitido, parabens!!")
else: 
    print("Vc n será admitido, tente outro ano!")

py = int(input("Quantos anos de experiencia em python vc tem? "))
ma = int(input("Quantos anos de experiencia vc tem e machine learning? "))
computação = input("Tem mestrado em ciencias da computação? ")

if computação =='sim': 
    computação = True
else:
    computação = False

if py >= 3 or computação or ma >= 2: 
    print("Vc é pode fazer sua canditatura!")
else: 
    print("Vc n pode fazer sua canditatura, vc n é qualificado!")
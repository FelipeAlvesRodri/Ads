salario = int(input("Qual o seu salario? "))
score = int(input("Qual seu score? "))
fia_score = int(input("Qual seu score do fiador? "))

if salario >= 2000 and (score >= 600 or fia_score >= 700):
    print("vc pode pegar o emprestimo!!")
else: 
    print("vc n esta qualificado para pegar o emprestimo!!")

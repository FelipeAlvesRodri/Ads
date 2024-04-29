gpa = float(input("Digite sua pontução: "))
top_10 = int(input("Qual foi seu rank da sua turma: "))
trabalho = int(input("Quantas horas vc trabalhou voluntariamente: "))
               
if gpa >= 3.5 or top_10 <= 10 or trabalho > 100 :
    print("Vc é legivel para a bolsa!")
else: 
    print("vc n é legivel para bolsa!")


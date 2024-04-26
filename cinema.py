idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("vc pode assistir ao filme")
else: 
    aco =  int(input("vc esta acomphado? (0 = n/ 1 = s)"))
 
if  aco == 1: 
 print("vc pode entrar!")   
else: 
    auto = int(input("vc está com uma autorização dos seus pais? (0 = n/ 1 = s) ")) 
    if  auto == 1: 
        print("vc pode entrar!!")
    else: 
        print("vc n pode entrar no cinema")
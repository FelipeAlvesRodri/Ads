def escolha_dia(dia): 
    dias ={
        1:"Segunda - Feira",
        2:"Terça - Feira",
        3:"Quarta - Feira",
        4:"Quinta - feira",
        5:"Sexta - Feira",
        6:"Sabado",
        7:"Domingo"
    }
    return dias.get(dia,"Dia invalido")

dia = int(input("Escolha um dia da semana "))
dia_selecionado = escolha_dia(dia)
print(f"O dia é:{dia_selecionado}")



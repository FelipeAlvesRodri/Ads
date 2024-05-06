ele_quimico = {
    "Fe": {"nr_atomico": 26, "nome":"Ferro", "massa": 55.845 },
    "Co": {"nr_atomico": 27, "nome": "Cobalto", "massa": 58.933 },
    "H": {"nr_atomico": 1, "nome": "Hidrogenio","massa": 1.008}
}

sigla = str(input("Qual a sigla do elemento: ")).upper()

if sigla in ele_quimico: 
    ele_quimico = ele_quimico[sigla]
    print(f"O seu elemento quimico é {ele_quimico['nome']} e sua sigla {sigla} ")
    print(f"O seu elemento quimico escolhido tem o numero atomico {ele_quimico['nr_atomico']} e a sua massa {ele_quimico ['massa']} ")

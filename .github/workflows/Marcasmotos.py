marcas = {
    "Honda":{"nome":"Honda CG 160","produção":2020,
             "peso": 19}, 
    "Kawasaki":{"nome": "NINJA ZX-4R", "produção": 2018,
                "peso":18 },
    "Shineray":{"nome": "ATV 200", 
                "produção": 2010, "peso":10},
    "Haojue":{"nome": "MASTER RIDE 150", 
             "produção": 2015, "peso":19},
    "BMW":{"nome": "BMW R 1250 GS", 
             "produção": 2020, "peso":20}
}

marcas_moto = input("Qual a marca que vc quer? ")

if marcas_moto in marcas:
    marcas = marcas[marcas_moto]
    print(f"o nome da moto {marcas['nome']}, produção {marcas['produção']}")
    print(f"o peso de sua moto é {marcas['peso']}kg")

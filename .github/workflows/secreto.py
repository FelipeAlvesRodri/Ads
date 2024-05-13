# Definindo a palavra secreta
palavra_secreta = "banana"

# Inicializando o número máximo de tentativas
tentativas_maximas = 3

# Inicializando a lista de letras já tentadas
letras_tentadas = []

# Inicializando a palavra oculta, mostrando apenas os espaços em branco
palavra_oculta = ["_"] * len(palavra_secreta)

# Loop principal do jogo
while tentativas_maximas > 0 and "_" in palavra_oculta:
    # Exibindo a palavra oculta atualizada
    print("Palavra: ", " ".join(palavra_oculta))
    
    # Exibindo as letras já tentadas
    print("Letras tentadas:", ", ".join(letras_tentadas))
    
    # Solicitando ao usuário uma letra
    letra = input("Digite uma letra: ").lower()
    
    # Verificando se a letra já foi tentada
    if letra in letras_tentadas:
        print("Você já tentou essa letra. Tente outra vez.")
        continue
    
    # Adicionando a letra à lista de letras tentadas
    letras_tentadas.append(letra)
    
    # Verificando se a letra está na palavra secreta
    if letra in palavra_secreta:
        print("Letra correta!")
        # Atualizando a palavra oculta com a letra correta
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_oculta[i] = letra
    else:
        print("Letra incorreta.")
        # Decrementando o número de tentativas restantes
        tentativas_maximas -= 1

# Verificando o resultado do jogo
if "_" not in palavra_oculta:
    print("Parabéns! Você acertou a palavra secreta:", "".join(palavra_oculta))
else:
    print("Você perdeu! A palavra secreta era:", palavra_secreta)

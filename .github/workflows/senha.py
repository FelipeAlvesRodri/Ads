# Laço para solicitar a senha até que ela atenda aos critérios
senha_valida = False
while not senha_valida:
    senha = input("Por favor, crie uma senha: ")
    
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres. Tente novamente.")
        continue
    
    # Verifica se a senha contém pelo menos um número e uma letra
    tem_numero = False
    tem_letra = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        elif caractere.isalpha():
            tem_letra = True
            
    if not (tem_numero and tem_letra):
        print("A senha deve conter números e letras. Tente novamente.")
        continue
    
    senha_valida = True

print("Senha válida! 👍")

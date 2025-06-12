#Variáveis
palavras = "python"
letrasChutadas = []
vidas = 5
ganho = False

while True:
    #Criar  lógica 
    for letra in palavras:
        if letra in letrasChutadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Voce tem {vidas} vidas restantes.")
    tentativa = input("Digite uma letra: ")
    letrasChutadas.append(tentativa.lower())
    if tentativa.lower() not in palavras.lower():
        vidas -= 1
    
    ganhou = True
    for letra in palavras:
        if letra.lower() not in letrasChutadas:
            ganhou = False

    if vidas == 0 or ganhou:
        break
    

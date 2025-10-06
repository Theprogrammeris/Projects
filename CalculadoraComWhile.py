while True:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite um outro número: ")
    sinal = input("Digite um sinal de: +-/*")

    numero_valido = None #cria-se uma variavel antes do try

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numero_valido = True #aqui ele executa como verdadeiro, ele vai tentar

    except:
        numero_valido = None #aqui você coloca na excceção, se for None

    if numero_valido is None:
        print("Digite algum número.")
        continue

    operadores_permitidos = "+-/*"

    if sinal not in operadores_permitidos:
        print("operador invalido")
        continue

    if len(sinal) > 1:
        print("Pode apenas 1 operador")
        continue

    print("Realizando conta...")

    if sinal == "+":
        print(f" sua soma é {numero1_float} + {numero2_float}= " , numero1_float + numero2_float)

    elif sinal == "-":
        print(f" sua subtração é {numero1_float} - {numero2_float}= " , numero1_float - numero2_float)

    elif sinal == "/":
        print(f" sua multiplicação é {numero1_float} / {numero2_float}= " , numero1_float / numero2_float)

    elif sinal == "*":
        print(f" sua multiplicação é {numero1_float} * {numero2_float}= ",  numero1_float * numero2_float)

    else:
        print("invalido, tente novamente")

    sair = input("Quem sair, digite (s) para sair.").lower()

    if sair is True:
        print("saindo...")
        break

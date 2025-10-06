while True:

    print("Seja bem vindo a calculadora,siga as instruções.")

    entrada1 = input("Digite um número: ")
    entrada2 = input("Digite um outro número: ")
    sinal = input("Coloque o sinal que deseja:(+-/*) ")

    try:
        entrada1_float = float(entrada1)
        entrada2_float = float(entrada2)
    
    except ValueError:
        print("Apenas números, tente novamente...")
        continue
    
    if sinal == None:
        print("Error, você tem que digitar algo.")
        continue
    elif sinal == "+":
        resultado = entrada1_float + entrada2_float
        print(f"Seu resultado é {entrada1_float} + {entrada2_float} = {resultado}")
    elif sinal == "-":
        resultado = entrada1_float - entrada2_float
        print(f"Seu resultado é {entrada1_float} - {entrada2_float} = {resultado}")
    elif sinal == "/":
        resultado = entrada1_float / entrada2_float
        print(f"Seu resultado é {entrada1_float} / {entrada2_float} = {resultado}")
    elif sinal == "*":
        resultado = entrada1_float * entrada2_float
        print(f"Seu resultado é {entrada1_float} * {entrada2_float} = {resultado}")
    else:
        print("Error, tente novamente.")
    sair = input("quer sair, digite (s)air").lower().strip()
    if sair == "s":
        print("Saindo , até mais.")
        break
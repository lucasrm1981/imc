# Solicita o nome do usuário e armazena na variável 'nome'
nome = input("Digite seu nome:\n")

# Solicita ao usuário se deseja calcular o IMC e armazena a resposta na variável 'opcao'
opcao = input("Você deseja calcular seu IMC? s/S ou qualquer tecla p/ sair?\n")

# Inicia um loop que continuará enquanto o usuário digitar 's' ou 'S'
while opcao == "s" or opcao == "S":
    # Solicita o peso do usuário e converte para um número de ponto flutuante, armazenando na variável 'peso'
    peso = float(input("Digite seu peso:\n"))

    # Solicita a altura do usuário e converte para um número de ponto flutuante, armazenando na variável 'altura'
    altura = float(input("Digite sua altura:\n"))

    # Calcula o IMC dividindo o peso pela altura ao quadrado e armazena o resultado na variável 'imc'
    imc = peso / (altura ** 2)

    # Verifica em qual faixa de IMC o valor calculado se enquadra e imprime a categoria correspondente
    if imc < 16:
        print(f"IMC = {imc:.2f} magreza grave")
    elif imc >= 16 and imc < 17:
        print(f"IMC = {imc:.2f} magreza moderada")
    elif imc >= 17 and imc <= 18.5:
        print(f"IMC = {imc:.2f} magreza leve")
    elif imc >= 18.6 and imc <= 24.9:
        print(f"IMC = {imc:.2f} peso ideal")
    elif imc >= 25 and imc <= 29.9:
        print(f"IMC = {imc:.2f} sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print(f"IMC = {imc:.2f} obesidade grau I")
    elif imc >= 35 and imc <= 39.9:
        print(f"IMC = {imc:.2f} obesidade grau II ou severa")
    elif imc > 40:
        print(f"IMC = {imc:.2f} obesidade grau III ou severa")

    # Solicita novamente ao usuário se deseja calcular o IMC e atualiza a variável 'opcao'
    opcao = input("Você deseja calcular seu IMC? s/S ou qualquer tecla p/ sair?\n")

    # Imprime um símbolo ":-)" na tela várias vezes, dependendo do valor do IMC
    for i in range(int(imc)):
        print(":-)" * int(imc))

# Imprime uma mensagem de despedida, incluindo o nome do usuário
print(f"Volte sempre, {nome}!")

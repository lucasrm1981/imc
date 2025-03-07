# Calcular o IMC através da fórmula e usar seus indices e textos dos indicadores, deve-se perguntar se o usuário deseja calcular o IMC e como saída posistiva ou não imprimir uma mensagem e o nome do usuário

# Fórmula peso / altura ao quadrado relembrando para fazer a potência de um número será o o numero ** potencia. exempo 3**2 = 9

# Indices do IMC
# resultados menores que 16 — saída: magreza grave;
# resultados entre 16 e 16,9 — saída:  magreza moderada;
# resultados entre 17 e 18,5 — saída:  magreza leve;
# resultados entre 18,6 e 24,9 — saída:  peso ideal;
# resultados entre 25 e 29,9 — saída:  sobrepeso;
# resultados entre 30 e 34,9 — saída:  obesidade grau I;
# resultados entre 35 e 39,9 — saída:  obesidade grau II ou severa;
# resultados maiores do que 40 — saída:  obesidade grau III ou mórbida.

# Serão utilizados: variáveis, while, for, if, elif, and, 

nome=input("Digite seu nome:\n")
opcao=input("Você deseja calcular seu IMC? s/S ou qualquer tecla p/ sair?\n")
while opcao=="s" or opcao=="S": # repetição caso a condição seja verdadeira
    peso=float(input("Digite seu peso:\n"))
    altura=float(input("Digite sua altura\n"))
    imc = peso/(altura**2)# imc recebe peso / altura ao quadrado
   
    if imc<16:
        print(f"IMC = {imc:.2f} magreza grave")
    elif imc>=16 and imc<17:
        print(f"IMC = {imc:.2f} magreza moderada")
    elif imc>=17 and imc<=18.5:
        print(f"IMC = {imc:.2f} magreza leve")
    elif imc>=18.6 and imc<=24.9:
        print(f"IMC = {imc:.2f} peso ideal")
    elif imc>=25 and imc<=29.9:
        print(f"IMC = {imc:.2f} sobrepeso")
    elif imc>=30 and imc<=34.9:
        print(f"IMC = {imc:.2f} obesidade grau I")
    elif imc>=35 and imc<=39.9:
        print(f"IMC = {imc:.2f} obesidade grau II ou severa")
    elif imc>40:
        print(f"IMC = {imc} obesidade grau III ou severa")
    
    opcao=input("Você deseja calcular seu IMC? s/S ou qualquer tecla p/ sair?\n")
    # Imprimir algo na tela
    for i in range(int(imc)): # Para o numero em um arranjo de 1 contando até o imc convertido em inteiro 
        print(":-)"*int(imc))# impressao do simbolo na linha

print(f" Volte sempre {nome} !")# fomartando nome dentro do texto
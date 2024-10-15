def soma(*args):
    resultado = sum(args)
    return resultado
def divisao(*args):
    if len(args) < 2:
        raise ValueError("Pelo menos dois números são necessários")
    resultado = args[0]
    for numero in args[1:]:
        resultado/= numero
def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
def subtracao(*args):
    if len(args) < 2:
        raise ValueError("Pelo menos dois números são necessários")
    resultado = [0]
    for numero in args[1:]:
        resultado -= numero
    return resultado

print("Digite uma opção de calculadora")
opcao = input("Digite: soma, subtração ou multiplicação ou subtração, de acordo com o que deseje ")

if(opcao == "soma"):
    
    entrada = input("Digite números separados por espaços: ")
    
    numeros = map(float,entrada.split())
    
    total = soma(*numeros)
    
    print("A soma dos números é: ", total)
elif(opcao == "subtração"):
    
    entrada = input("Digite números separados por espaços: ")
   
    numeros = map(float, entrada.slipt())
    
    total = subtracao(*numeros)
    
    print("A soma dos números é: ". total2)
elif(opcao == "multiplicação"):
    entrada = input("Digite um número separado por espaços: ")
    
    numeros = map(float, entrada.split())
    
    total = multiplicacao(*numeros)
    
    print("O resultado total é: ", total)
    
elif(opcao == "divisão"):
    entrada = input("Digite um número separado por espaços: ")
    numeros = list(map(float, entrada.split()))
    try:
        total = divisao(*numeros)
        print("O resultado da divisão é: ", total)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida")
    else: 
        print("Opção inválida. Por favor selecione uma válida")
    
    

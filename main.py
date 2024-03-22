import sys

def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    return a / b

args = sys.argv[1:]

#print(args)

operacao = args[0]
a = int(args[1])
b = int(args[2])
resultado = 0

if operacao == "soma":
    resultado = soma(a,b)

if operacao == "subtracao":
    resultado = subtracao(a,b)

if operacao == "multiplicacao":
    resultado = multiplicacao(a,b)

if operacao == "divisao":
    resultado = divisao(a,b)

print (resultado)



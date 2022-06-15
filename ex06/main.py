numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

operacao = numero1+numero2

if (operacao > 50):
    resultado = operacao+18

else:
    resultado = operacao-15

print("\nresultado é {} " .format(resultado))

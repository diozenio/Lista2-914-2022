while(1==1):
  numero = int(input('Informe o número:'))
  x = 0
  for i in range(1,numero):
    if(numero % i == 0):
        x = x + 1
          
  if (x<=1):
    print("Número primo\n")
  else:
    print("Número não é primo\n")
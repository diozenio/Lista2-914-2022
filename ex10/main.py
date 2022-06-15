import random
while(1==1):
  print("APERTE [1] PARA LISTA DE NOMES: ")
  print("APERTE [2] PARA LISTA DE NÚMEROS: ")
  x = int(input(''))
  
  if(x==1):
    a = (input('\nInforme o primeiro nome:'))
    b = (input('Informe o segundo nome:'))
    c = (input('Informe o terceiro nome:'))

    aleatorio = random.sample((a,b,c), 3)
    
    print("Lista:", aleatorio, "\n") 
    
  elif (x==2):
    n = int(input('\nInforme o primeiro número:'))
    m = int(input('Informe o segundo número:'))
    o = int(input('Informe o terceiro número:'))

    aleatorio = random.sample((n,m,o), 3)
    
    print("Lista: ", aleatorio, "\n") 

  else:
    print("O NÚMERO {} NÃO É VÁLIDO!\n" .format(x))
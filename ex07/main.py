while(1==1):
  numero = int(input('\nDigite o número para ver o dia semana: '))

  if (numero>=1 and numero<=7):
    
   if (numero == 1):
      print ("O dia correspondente ao número {} é domingo" .format(numero))
      
   if (numero == 2):
     print ("O dia correspondente ao número {} é segunda" .format(numero))

   if (numero == 3):
    print ("O dia correspondente ao número {} é terça" .format(numero))

   if (numero == 4):
    print ("O dia correspondente ao número {} é quarta" .format(numero))

   if (numero == 5):
    print ("O dia correspondente ao número {} é quinta" .format(numero))

   if (numero == 6):
    print ("O dia correspondente ao número {} é sexta" .format(numero))

   if (numero == 7):
    print ("O dia correspondente ao número {} é sábado" .format(numero))

  else:
    print ("Não há um dia da semana correspondente ao número {}".format(numero))
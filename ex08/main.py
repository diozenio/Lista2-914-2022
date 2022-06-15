diaAtual = int(input('Digite o dia de hoje: '))
mesAtual = int(input('Digite o mês atual: '))
anoAtual = int(input('Digite o ano atual: '))

diaVenc = int(input('\nDigite o dia de vencimento: '))
mesVenc = int(input('Digite o mês de vencimento: '))
anoVenc = int(input('Digite o ano de vencimento '))

if (anoVenc<anoAtual):
  print ("\nProduto está vencido!")

elif (anoVenc==anoAtual):
  
  if (mesVenc<mesAtual):
    print ("\nProduto vencido!")

  elif (mesVenc>mesAtual):
    print ("\nProduto não está vencido!" )

  elif (mesVenc == mesAtual):
       if (diaVenc<diaAtual):
            print ("\nProduto está vencido!" )

       elif (diaVenc>diaAtual):
            print ("\nProduto não está vencido!" )

       else:
            print ("\nHoje é o dia do vencimento deste produto!" )

else:
  print ("\nProduto não está vencido!")
print('Is de kaas geel?, typ 1 voor ja en 2 voor nee')
kaas = int(input())
nee = 2
if nee > kaas:
  print('zitten er gaten in?')
  gaten = int(input())
  if nee > gaten:
   print('Is de kaas belachelijk duur?')
   duur = int(input())
   if nee > duur:
         print('De kaas is Emmenthaler!')
   else: 
        print('De kaas is Leerdammer!')
  else:
   print('Is de kaas hard als steen?')
   steen = int(input())
   if nee > steen:
       print('De kaas is Parmigiano Reggiano!')
   else: 
       print('De kaas is Goudse kaas!')
else:  
  print('heeft de kaas blauwe schimmel?')
  schimmel = int(input())
  if nee > schimmel:
      print('Heeft de kaas een korst?')
      korst = int(input())
      if nee > korst:
          print('De kaas is Bleu de rochbaron!')
      else:
          print("De kaas is Foume D'ambert!")
  else:
    print('Heeft de kaas een korst?')
    kaaskorst = int(input())
    if nee > kaaskorst:
        print('De kaas is Camembert!')
    else:
        print('De kaas is mozzarella!')
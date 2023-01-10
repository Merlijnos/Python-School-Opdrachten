print('------------------------------------------------')
print('    - Solicitatieformulier Circusdirecteur -    ')
print('------------------------------------------------')
print('Er worden zo een paar vragen gesteld.           ')
print('typ 1 voor ja en 2 voor nee.')
print('Beantwoord de vragen eerlijk en denk niet te moeilijk.')
print('Success! :)')
print('------------------------------------------------')
nee = 2
naam = input('Wat is uw naam? ')
print('Hallo ' + naam + '!')
print('Hoeveel jaar Heeft u praktijkervaring met dieren-dressuur, jongleren of praktijkervaring met acrobatiek?')
vraag1 = input()
if int(vraag1) > int(2):
    print('Heeft u een MBO-4 diploma voor ondernemen?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag2 = input()
if nee > int(vraag2):
    print('Bent u in bezit van een geldig vrachtwagen bewijs?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag3 = input()
if nee > int (vraag3):
    print('Bent u in bezit van een hoge hoed?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag4 = input()
if nee > int(vraag4):
    print('Bent u een man met een snor van 10cm of breder, of een vrouw met rood haar langer dan 20cm?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag5 = input()
if nee > int(vraag5):
    print('Hoe lang bent u?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag6 = input()
if int(150) < int(vraag6):
    print('Wat is uw lichaamsgewicht in kilos?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag7 = input()
if int(90) < int(vraag7):
    print('Heeft u het certificaat “Overleven met gevaarlijk personeel”?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag8 = input()
if nee > int(vraag8):
    print('heeft u een hond?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag9 = input()
if nee > int(vraag9):
    print('Kunt u springen?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag10 = input()
if nee > int(vraag10):
    print('Bent u moordlustig?')
else:
    print('Sorry, u bent niet geschikt als circusdirecteur.')
vraag11 = input()
if nee > int(vraag11):
    print('Lust u appels?')
else:
    print('Sorry, u bent bij de laatste vraag afgezakt en daardoor niet geschikt als circusdirecteur.')
vraag12 = input()
print('Dit is het einde van het solicitatieformulier, bedankt voor het invullen.')
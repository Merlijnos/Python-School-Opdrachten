import random
import sys
for i in range(20):
    score = 0
    ronde = 0
    ronde += 1
    pogingen = 0
    Getal = random.randint(1,1000)
    while pogingen < 10 :
        pogingen += 1
        print('Probeer het nummer te raden!')
        invoer = int(input())
        if invoer == Getal:
            pogingen = 10
            score += 1
            print('U heeft het getal geraden! Uw score is nu',score)
            answer = input('Wilt u nog een ronde? Ja/Nee ')
            if answer == 'nee' or answer == 'Nee':
                sys.exit()      
        elif abs(Getal - int(invoer)) <= 20:
            print('U zit heel warm')
        elif abs(Getal - int(invoer)) <= 50:
            print('U zit warm') 
        elif abs(Getal - int(invoer)) >= 20:
            print('U zit koud')
        elif abs(Getal - int(invoer)) >= 50:
            print('U zit heel koud')
    print('Ronde is',ronde,'Score is',score)
    

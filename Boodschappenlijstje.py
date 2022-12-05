boodschappenlijst = {}
opnieuw = True
while opnieuw == True:
    vrg = input('Wilt u iets toevoegen? ja/nee : ').capitalize()
    if vrg == 'Ja':
        product = input('Wat wilt u toevoegen : ').capitalize()
        aantal = int(input('Hoeveel '+ product +' Wilt u? : '))
        if product in boodschappenlijst.keys():
            boodschappenlijst[product] += (aantal)
        else:
            boodschappenlijst[product] = aantal
        print(boodschappenlijst)
    else:
        print('-[ BOODSCHAPPENLIJST ]-')
        print(boodschappenlijst)
        opnieuw = False
        print('___________________')
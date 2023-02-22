def survival():
    score = 0
    repeat = True
    while repeat == True:
        print('Welkom bij survival!')
        input('Klik op ENTER om te beginnen')

        input('Je wordt wakker in een grot, je ligt op een steen en er staat een rugzak met een paar spullen om te beginnen.')
        Option1 = input('Kijk in de rugtas? Typ 1 voor JA en 2 voor NEE ')
        while Option1 == "":
            print("Je moet een keuze maken!")
            Option1 = input('Kijk in de rugtas? Typ 1 voor JA en 2 voor NEE ')
        if Option1 == '1':
            score += 1
            input('Je vind een stok, een paar stenen en een touw')
            Option2 = input('Ga op pad? Typ 1 voor JA en 2 voor NEE ')
            while Option2 == "":
                print("Je moet een keuze maken!")
                Option2 = input('Ga op pad? Typ 1 voor JA en 2 voor NEE ')
            if Option2 == '1':
                score += 1
                input(
                    'Je stapt binnen in een bos, de bomen komen boven de wolken uit, je ziet ook een paar wezens in de lucht.')
                Option3 = input('Maak een bijl? Typ 1 voor JA en 2 voor NEE ')
                while Option3 == "":
                    print("Je moet een keuze maken!")
                    Option3 = input(
                        'Maak een bijl? Typ 1 voor JA en 2 voor NEE ')
                if Option3 == '1':
                    score += 1
                    input('Er komt één van de vogelachtige beesten recht op je af')
                    input(
                        'Hij valt je aan, gelukkig heb je een bijl bij de hand waar je jezelf mee kan verdedigen')
                    input(
                        'Het beest heeft een lichtgevende steen in het midden van zijn hoofd je kan er moeilijk bij omdat het beest zo groot is')
                    Option4 = input(
                        'gooi de bijl? Typ 1 voor JA en 2 voor NEE ')
                    while Option4 == "":
                        print("Je moet een keuze maken!")
                        Option4 = input(
                            'gooi de bijl? Typ 1 voor JA en 2 voor NEE ')
                    if Option4 == '1':
                        score += 1
                        input(
                            'Je gooit de bijl naar de steen toe, het explodeert en het wezen ligt in duizend stukken')
                        input(
                            'Je hebt gewonnen! Je besluit verder te gaan alsof er niks gebeurd was, gelukkig ben je nu voorbereid als het nog eens gebeurt.')
                        Option5 = input(
                            'Je ziet een pad in de verte, volg het pad? Typ 1 voor JA en 2 voor NEE ')
                        while Option5 == "":
                            print("Je moet een keuze maken!")
                            Option5 = input(
                                'Je ziet een pad in de verte, volg het pad? Typ 1 voor JA en 2 voor NEE ')
                        if Option5 == '1':
                            score += 1
                            input(
                                'Na een uur lang lopen zie je in de verte een rookpluim')
                            input('Je gaat rechtstreeks naar de rookpluim toe')
                            Option6 = input(
                                'Je ziet een dorp, het lijkt erop dat er andere mensen wonen. Ga naar binnen? Typ 1 voor JA en 2 voor NEE ')
                            while Option6 == "":
                                print("Je moet een keuze maken!")
                                Option6 = input(
                                    'Je ziet een dorp, het lijkt erop dat er andere mensen wonen. Ga naar binnen? Typ 1 voor JA en 2 voor NEE ')
                            if Option6 == '1':
                                score += 1
                                input(
                                    'Je kan zo naar binnen stappen, er is eten, medicijnen en onderdak')
                                Option7 = input(
                                    'Je wordt vriendelijk ontvangen en je krijgt een tent aangeboden om in te slapen. Accepteer dit aanbod? Typ 1 voor JA en 2 voor NEE ')
                                while Option7 == "":
                                    print("Je moet een keuze maken!")
                                    Option7 = input(
                                        'Je wordt vriendelijk ontvangen en je krijgt een tent aangeboden om in te slapen. Accepteer dit aanbod? Typ 1 voor JA en 2 voor NEE ')
                                if Option7 == '1':
                                    score += 3
                                    input(
                                        'je gaat slapen, het is een tijd geleden dat je in een zacht bed heb geslapen. Hier voel je je veilig.')
                                    input('The End')
                                    input('Je hebt ' + str(score) +
                                          ' punten behaald!')
                                    nogeenkeer = input(
                                        'Wil je nog een keer spelen? JA of NEE ').lower()
                                    if nogeenkeer == 'ja':
                                        repeat = True
                                    else:
                                        repeat = False
                                else:
                                    input(
                                        'Je besluit te gaan slapen buiten de muur, maar de mensen denken dat je een orc bent.')
                                    input(
                                        'De mensen roepen naar je maar je ligt zo diep in slaap dat je hun niet hoort')
                                    input(
                                        'Na 5 minuten roepen schieten ze, een pijl gaat recht door je hoofd, het is klaar')
                                    input('GAME OVER')
                                    input('Je hebt ' + str(score) +
                                          ' punten behaald!')
                                    nogeenkeer = input(
                                        'Wil je nog een keer spelen? JA of NEE ').lower()
                                    if nogeenkeer == 'ja':
                                        repeat = True
                                    else:
                                        repeat = False
                            else:
                                input(
                                    'Je gaat niet naar binnen, hetgene waar je de hele tijd voor gezocht hebt ga je nu niet heen')
                                input(
                                    'Waarom? Ben je bang? ALs je niet gaat sterf je waarschijnlijk van de honger')
                                Option8 = input(
                                    'Wil je toch nog naar binnen? Typ 1 voor JA en 2 voor NEE ')
                                if Option8 == '1':
                                    score += 3
                                    input(
                                        'Je gaat naar binnen, het is al middernacht maar nadat je de mensen uitlegt wat er is gebeurt wordt je toch binnengelaten')
                                    input('The End')
                                    input('Je hebt ' + str(score) +
                                          ' punten behaald!')
                                    nogeenkeer = input(
                                        'Wil je nog een keer spelen? JA of NEE ').lower()
                                    if nogeenkeer == 'ja':
                                        repeat = True
                                    else:
                                        repeat = False
                        else:
                            input(
                                'Je gaat dwars door de bossen heen, hopend dat je een onderdak voor de nacht vind')
                            input('Het is pikkedonker en je hebt nog niks gevonden.')
                            Option9 = input(
                                'je vind een hol in een boom, ga naar binnen? Typ 1 voor JA en 2 voor NEE ')
                            if Option9 == '1':
                                input(
                                    'Er ligt een zachte deken binnen, hoe komt die daar?')
                                input(
                                    'Opeens hoor je gegrom, de deken begint te bewegen')
                                input(
                                    'Het was een beer!, de beer grijpt je vast en knuffelt je dood')
                                input('GAME OVER')
                                input('Je hebt ' + str(score) +
                                      ' punten behaald!')
                                nogeenkeer = input(
                                    'Wil je nog een keer spelen? JA of NEE ').lower()
                                while nogeenkeer == "":
                                    print("Je moet een keuze maken!")
                                    nogeenkeer = input(
                                        'Wil je nog een keer spelen? JA of NEE ').lower()
                                if nogeenkeer == 'ja':
                                    repeat = True
                                else:
                                    repeat = False
                            else:
                                score += 2
                                input(
                                    'Je loopt verder door, je had een slecht gevoel bij die boom...')
                                input('Je hoort een harde brul in de verte')
                                option10 = input(
                                    'Ga ernaartoe? Typ 1 voor JA en 2 voor NEE ')
                                if option10 == 1:
                                    input(
                                        'Het was al vrij logisch dat het gevaar was...')
                                    input(
                                        'Wat er daarna gebeurde is te heftig om te vertellen')
                                    input('GAME OVER')
                                    input('Je hebt ' + str(score) +
                                          ' punten behaald!')
                                    nogeenkeer = input(
                                        'Wil je nog een keer spelen? JA of NEE ').lower()
                                    while nogeenkeer == "":
                                        print("Je moet een keuze maken!")
                                        nogeenkeer = input(
                                            'Wil je nog een keer spelen? JA of NEE ').lower()
                                    if nogeenkeer == 'ja':
                                        repeat = True
                                    else:
                                        repeat = False
                                else:
                                    score += 3
                                    input(
                                        'Je valt door de grond en je komt terug in de realiteit')
                                    input(
                                        'Het was een droom? maar het voelde zo echt!')
                                    input(
                                        'Je wordt bezweet wakker, in je eigen bed')
                                    input('The End')
                                    input('Je hebt ' + str(score) +
                                          ' punten behaald!')
                                    nogeenkeer = input(
                                        'Wil je nog een keer spelen? JA of NEE ').lower()
                                    while nogeenkeer == "":
                                        print("Je moet een keuze maken!")
                                        nogeenkeer = input(
                                            'Wil je nog een keer spelen? JA of NEE ').lower()
                                    if nogeenkeer == 'ja':
                                        repeat = True
                                    else:
                                        repeat = False
                    else:
                        input(
                            'Je probeert het beest te raken maar hij is zo groot dat je niet bij de kop kan komen')
                        input('Hij pakt je arm en scheurt je in stukken')
                        input('The End')
                        input('Je hebt ' + str(score) + ' punten behaald!')
                        nogeenkeer = input(
                            'Wil je nog een keer spelen? JA of NEE ').lower()
                        while nogeenkeer == "":
                            print("Je moet een keuze maken!")
                            nogeenkeer = input(
                                'Wil je nog een keer spelen? JA of NEE ').lower()
                        if nogeenkeer == 'ja':
                            repeat = True
                        else:
                            repeat = False
                else:
                    input('Je valt door een gat in de grond naar beneden')
                    input('Je leeft nog maar je ziet niks')
                    input('Opeens komt er een megaspin uit het donker op je af rennen')
                    input('je valt om van de schok en wordt levend opgegeten.')
                    input('GAME OVER')
                    input('Je hebt ' + str(score) + ' punten behaald!')
                    nogeenkeer = input(
                        'Wil je nog een keer spelen? JA of NEE ').lower()
                    while nogeenkeer == "":
                        print("Je moet een keuze maken!")
                        nogeenkeer = input(
                            'Wil je nog een keer spelen? JA of NEE ').lower()
                    if nogeenkeer == 'ja':
                        repeat = True
                    else:
                        repeat = False
            else:
                input('Je slaapt weer verder , misschien is het gewoon een droom...')
                input('Helaas werd je nooit meer wakker omdat de nacht te koud was')
                input('GAME OVER')
                input('Je hebt ' + str(score) + ' punten behaald!')
                nogeenkeer = input(
                    'Wil je nog een keer spelen? JA of NEE ').lower()
                while nogeenkeer == "":
                    print("Je moet een keuze maken!")
                    nogeenkeer = input(
                        'Wil je nog een keer spelen? JA of NEE ').lower()
                if nogeenkeer == 'ja':
                    repeat = True
                else:
                    repeat = False
        else:
            input('Je gaat naar buiten zonder spullen')
            input('Er zit iets achter je aan, je weet niet wat het is')
            input('Je hoort het beest steeds dichterbij komen, hij haalt je in!')
            input(
                'Je wordt opgegeten en er blijft niks van je over, had je maar in die rugtas gekeken...')
            input('GAME OVER')
            input('Je hebt ' + str(score) + ' punten behaald!')
            nogeenkeer = input(
                'Wil je nog een keer spelen? JA of NEE ').lower()
            while nogeenkeer == "":
                print("Je moet een keuze maken!")
                nogeenkeer = input(
                    'Wil je nog een keer spelen? JA of NEE ').lower()
            if nogeenkeer == 'ja':
                repeat = True
            else:
                repeat = False
survival()
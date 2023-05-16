from functies import welkom, vraag_aantal_bolletjes, geef_ijs, vraag_meer_bestellen, bonnetje

def bestelling_opnemen():
    welkom()

    bestellingen = []

    while True:
        aantal_bolletjes, bakje_of_hoorntje = vraag_aantal_bolletjes()
        if aantal_bolletjes and bakje_of_hoorntje:
            geef_ijs(aantal_bolletjes, bakje_of_hoorntje)
            bestellingen.append((aantal_bolletjes, bakje_of_hoorntje))

        if not vraag_meer_bestellen():
            print(bonnetje(bestellingen))
            break

bestelling_opnemen()

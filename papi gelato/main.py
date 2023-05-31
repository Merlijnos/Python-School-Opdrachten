from functies import welkom, vraag_aantal_bolletjes, vraag_smaak, geef_ijs, vraag_meer_bestellen, print_receipt

def bestelling_opnemen():
    welkom()

    bestellingen = []

    while True:
        aantal_bolletjes, bakje_of_hoorntje = vraag_aantal_bolletjes()
        if aantal_bolletjes is not None and bakje_of_hoorntje is not None:
            smaken = vraag_smaak(aantal_bolletjes)
            geef_ijs(aantal_bolletjes, bakje_of_hoorntje)
            bestellingen.append((aantal_bolletjes, bakje_of_hoorntje, smaken))

        if not vraag_meer_bestellen():
            print_receipt(bestellingen)
            break

bestelling_opnemen()
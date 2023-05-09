from functies import welkom, vraag_aantal_bolletjes, geef_ijs, vraag_meer_bestellen

def bestelling_opnemen():
    welkom()
    
    while True:
        aantal_bolletjes, bakje_of_hoorntje = vraag_aantal_bolletjes()
        if aantal_bolletjes and bakje_of_hoorntje:
            geef_ijs(aantal_bolletjes, bakje_of_hoorntje)

        if not vraag_meer_bestellen():
            print("Bedankt en tot ziens!")
            break

if __name__ == "__main__":
    bestelling_opnemen()

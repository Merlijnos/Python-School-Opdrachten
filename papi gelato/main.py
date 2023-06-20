from functies import vraag_aantal_bolletjes, vraag_bakje_of_hoorntje, vraag_smaak, vraag_topping, print_receipt

def main():
    bestellingen = []
    while True:
        nieuwe_bestelling = input("Wilt u een nieuwe bestelling starten? (ja/nee) ")
        if nieuwe_bestelling.lower() == "ja":
            aantal_bolletjes = vraag_aantal_bolletjes()
            bakje_of_hoorntje = vraag_bakje_of_hoorntje()
            smaken = vraag_smaak(aantal_bolletjes)
            topping = vraag_topping(bakje_of_hoorntje)
            bestellingen.append((aantal_bolletjes, bakje_of_hoorntje, smaken, topping))
        elif nieuwe_bestelling.lower() == "nee":
            print_receipt(bestellingen)
            break
        else:
            print("Sorry dat snap ik niet...")

if __name__ == "__main__":
    main()
def welkom():
    print("Welkom bij Papi Gelato! Hieronder ziet u onze beschikbare smaken:")

def vraag_aantal_bolletjes():
    while True:
        aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")
        if aantal_bolletjes.isdigit():
            aantal_bolletjes = int(aantal_bolletjes)
            if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
                bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
                while bakje_of_hoorntje.lower() not in ["hoorntje", "bakje"]:
                    print("Sorry, dat snap ik niet...")
                    bakje_of_hoorntje = input("Wilt u deze bolletjes in een hoorntje of een bakje? ")
                return aantal_bolletjes, bakje_of_hoorntje
            elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
                return aantal_bolletjes, "bakje"
            elif aantal_bolletjes > 8:
                print("Sorry, zulke grote bakken hebben we niet.")
            else:
                print("Sorry, dat snap ik niet...")
        else:
            print("Sorry, dat snap ik niet...")

def geef_ijs(aantal_bolletjes, bakje_of_hoorntje):
    if bakje_of_hoorntje == "hoorntje":
        print(f"Hier is uw hoorntje met {aantal_bolletjes} bolletje(s).")
    elif bakje_of_hoorntje == "bakje":
        print(f"Hier is uw bakje met {aantal_bolletjes} bolletje(s).")

def vraag_meer_bestellen():
    while True:
        meer_bestellen = input("Wilt u nog meer bestellen? ")
        if meer_bestellen.lower() == "ja":
            return True
        elif meer_bestellen.lower() == "nee":
            return False
        else:
            print("Sorry, dat snap ik niet...")

def bonnetje(bestellingen):
    print("-----------[" + "Papi Gelato" + "]-----------")
    totaal_prijs = 0
    totaal_bolletjes = 0
    totaal_bakjes = 0
    totaal_hoorntjes = 0

    prijs_bolletje = 1.10
    prijs_bakje = 0.75
    prijs_hoorntje = 1.25

    for aantal_bolletjes, bakje_of_hoorntje in bestellingen:
        prijs = prijs_bolletje * aantal_bolletjes
        if bakje_of_hoorntje == "bakje":
            prijs += prijs_bakje
            totaal_bakjes += 1
        elif bakje_of_hoorntje == "hoorntje":
            prijs += prijs_hoorntje
            totaal_hoorntjes += 1

        totaal_bolletjes += aantal_bolletjes
        totaal_prijs += prijs

    print(f"Totaal bolletjes:    {totaal_bolletjes} X €1.10 = €{totaal_bolletjes * prijs_bolletje:.2f}")
    print(f"Totaal bakjes:       {totaal_bakjes} X €0.75 = €{totaal_bakjes * prijs_bakje:.2f}")
    print(f"Totaal hoorntjes:    {totaal_hoorntjes} X €1.25 = €{totaal_hoorntjes * prijs_hoorntje:.2f}")
    print("-------------------------------------")
    print(f"Totaal =             €{totaal_prijs:.2f}")
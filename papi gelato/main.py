from functies import *

def main():
    while True:
        klant_type = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ")
        while klant_type not in ["1", "2"]:
            print("Sorry, dat is geen geldige keuze. Probeer het opnieuw.")
            klant_type = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ")
        bestellingen = []
        while True:
            if klant_type == "1":
                aantal_bolletjes = vraag_aantal_bolletjes()
                bakje_of_hoorntje = vraag_bakje_of_hoorntje(aantal_bolletjes)
                smaken = vraag_smaak(aantal_bolletjes)
                topping = vraag_topping(bakje_of_hoorntje)
                bestellingen.append((aantal_bolletjes, bakje_of_hoorntje, smaken, topping))
            elif klant_type == "2":
                aantal_liters = vraag_aantal_bolletjes(is_zakelijk=True)
                smaken = vraag_smaak(aantal_liters)
                toon_prijs(aantal_liters, smaken, is_zakelijk=True)
            else:
                print("Sorry dat snap ik niet...")
            opnieuw_bestellen = input("Wilt u nog een bestelling plaatsen? (ja/nee) ")
            if opnieuw_bestellen.lower() == "nee":
                break
        if klant_type == "1":
            print_receipt(bestellingen)
        nog_een_keer = input("Wilt u nog een bestelling plaatsen? (ja/nee) ")
        if nog_een_keer.lower() == "nee":
            break

def toon_prijs(aantal_liters, smaken, is_zakelijk=False):
    prijs_per_liter = 9.80 if is_zakelijk else 6.25
    totaal_prijs = aantal_liters * prijs_per_liter
    btw = totaal_prijs * 0.09 if is_zakelijk else 0
    smaken_dict = {}
    for smaak in smaken:
        if smaak in smaken_dict:
            smaken_dict[smaak] += 1
        else:
            smaken_dict[smaak] = 1
    print("----- Papi Gelato -----")
    print("Bestelling: ")
    for i, (smaak, aantal) in enumerate(smaken_dict.items()):
        print(f"{aantal} x {smaak}")
    print(f"\nAantal liter(s): {aantal_liters}")
    print(f"Totaalprijs: €{totaal_prijs:.2f}")
    if is_zakelijk:
        print(f"BTW (9%): €{btw:.2f}")
    print("------------------------")

if __name__ == "__main__":
    main()
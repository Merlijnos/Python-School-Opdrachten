import functies

def main():
    functies.print_welcome_message()
    bestellingen = functies.vraag_bestellingen()
    functies.vraag_meer_bestellingen(bestellingen)

if __name__ == "__main__":
    main()
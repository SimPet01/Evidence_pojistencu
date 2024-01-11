class Prostredi:
    """
    Třída upravuje, co vidí uživatel aplikace
    """

    def vypis_nadpis(self):
        """
        Vypíše nadpis aplikace
        """
        print(" _________________________\n   Evidence pojištěných \n _________________________\n\n")


    def vyber_akci(self):
        """
        Vypíše uživateli možnosti z výběru úkonů
        """
        print("Vyberte číslo jedné z následujících akcí:\n"
              "1 - Přidat nového pojištěného\n"
              "2 - Vypsat všechny pojištěné\n"
              "3 - Vyhledat pojištěného\n"
              "4 - Ukončení aplikace\n")


    def _vycisti_obrazovku(self):
        """
        Vyčištění obrazovky konzole

        Bohužel '_vycisti_obrazovku' v PyCharmu nefunguje tak, jak bych očekával - obrazovka konzole se nevyčistí,
        vypíše se jen '?' ve čtverečku
        """
        import sys as _sys
        import subprocess as _subprocess
        # kontrola na jakém operačním systému je tato aplikace spuštěna
        if _sys.platform.startswith("win"):
            # v případě OS Windows použití následujících instrukcí: ["otevření příkazového řádku", "ukončení běhu aplikace", "vyčištění obrazovky konzole"]
            _subprocess.run(["cmd.exe", "/C", "cls"])
        else:
            # instrukce pro případ použití OS MacOS; ostatní OS jsem zanedbal
            _subprocess.call("clear")


    def zobraz_nadpis_akci(self):
        """
        Úvodní vítací obrazovka po spuštění aplikace a po každé hotové volbě

        """
        prostredi._vycisti_obrazovku()
        prostredi.vypis_nadpis()
        prostredi.vyber_akci()


    def zobraz_nadpis(self):
        """
        Načetla by se tím hlavička aplikace při jejím ukončením

        """
        prostredi._vycisti_obrazovku()
        prostredi.vypis_nadpis()


    def osetri_text_input(self, pobidka):
        """
        Ošetření vstupních dat od uživatele pro jméno a příjmení

        Parametry:
            :param pobidka: Parametr vepsaný v 'povely.py'
        """
        while True:
            # místo 'pobídky' se vloží parametr vepsaný v povely.py
            user_input = input(pobidka)
            # pro všechny řetězce musí platit, že jsou textem nebo mezerou
            if user_input and all((x.isalpha() or x.isspace()) for x in user_input):
                # první [0] znak z řetězce je kapitálkou
                if user_input[0].isupper():
                    return user_input
                else:
                    print("První písmeno by mělo být velké.")
            else:
                print("Vstup by měl obsahovat pouze písmena a mezery.")


    def osetri_vek_input(self):
        """
        Ošetření vstupu pro věk

        """
        while True:
            vek = input("Zadejte věk: ")
            # zadaný input je číslo
            if vek.isdigit():
                vek = int(vek)
                # podmínka pro smysluplné číslo náležející věku
                if 1 <= vek <= 120:
                    return vek
                else:
                    print("Věk by měl být v rozmezí 1 až 120 let.")
            else:
                print("Věk by měl být zadán jako číslo.")


    def osetri_telefon_input(self):
        """
        Ošetření vstupu pro telefon

        """
        while True:
            telefon = input("Zadejte telefon: ")
            # zadaný input je číslo
            if telefon.isdigit():
                # podmínka, že číslo má devět cifer
                if len(telefon) == 9:
                    return int(telefon)
                else:
                    print("Telefon by měl obsahovat devět cifer.")
            else:
                print("Telefon by měl být zadán jako číslo.")


prostredi = Prostredi()

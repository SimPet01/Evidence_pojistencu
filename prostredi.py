class Prostredi:
        # třída upravuje co vidí uživatel aplikace
    def vypis_nadpis(self):
        print(" _________________________\n   Evidence pojištěných \n _________________________\n\n")   # nadpis aplikace

    def vyber_akci(self):                                           # možnosti z výběru úkonů
        print("Vyberte číslo jedné z následujících akcí:\n"
                "1 - Přidat nového pojištěného\n"
                "2 - Vypsat všechny pojištěné\n"
                "3 - Vyhledat pojištěného\n"
                "4 - Ukončení aplikace\n")

    """ '_vycisti_obrazovku' v PyCharmu nefunguje, jak bych očekával - obrazovka konzole se nevyčistí, vypíše se jen '?' ve čtverečku """

    def _vycisti_obrazovku(self):                       # vyčištění obrazovky konzole
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):             # kontrola na jakém operačním systému je tato aplikace spuštěna
            _subprocess.run(["cmd.exe", "/C", "cls"])   # v případě OS Windows použití následujících instrukcí: ["otevření příkazového řádku", "ukončení běhu aplikace", "vyčištění obrazovky konzole"]
        else:
            _subprocess.call("clear")                   # instrukce pro případ použití OS MacOS; ostatní OS jsem zanedbal

    def zobraz_nadpis_akci(self):                       # úvodní vítací obrazovka po spuštění aplikace a po každé hotové volbě se mohla spustit
        prostredi._vycisti_obrazovku()
        prostredi.vypis_nadpis()
        prostredi.vyber_akci()

    def zobraz_nadpis(self):                            # načetla by se tím hlavička aplikace při jejím ukončením
        prostredi._vycisti_obrazovku()
        prostredi.vypis_nadpis()

    def osetri_text_input(self, pobidka):               # ošetření vstupu pro jméno a příjmení
        while True:
            user_input = input(pobidka)                 # místo 'pobídky' se vloží parametr vepsaný v povely.py
            if user_input and all((x.isalpha() or x.isspace()) for x in user_input):    # pro všechny řetězce musí platit, že jsou textem nebo mezerou
                if user_input[0].isupper():                                             # první [0] znak z řetězce je kapitálkou
                    return user_input
                else:
                    print("První písmeno by mělo být velké.")
            else:
                print("Vstup by měl obsahovat pouze písmena a mezery.")

    def osetri_vek_input(self):                         # ošetření vstupu pro věk
        while True:
            vek = input("Zadejte věk: ")
            if vek.isdigit():                           # zadaný input je číslo
                vek = int(vek)
                if 1 <= vek <= 120:                     # podmínka pro smysluplné číslo náležející věku
                    return vek
                else:
                    print("Věk by měl být v rozmezí 1 až 120 let.")
            else:
                print("Věk by měl být zadán jako číslo.")

    def osetri_telefon_input(self):                     # ošetření vstupu pro telefon
        while True:
            telefon = input("Zadejte telefon: ")
            if telefon.isdigit():                       # zadaný input je číslo
                if len(telefon) == 9:                   # podmínka, že číslo má devět cifer
                    return int(telefon)
                else:
                    print("Telefon by měl obsahovat devět cifer.")
            else:
                print("Telefon by měl být zadán jako číslo.")


prostredi = Prostredi()

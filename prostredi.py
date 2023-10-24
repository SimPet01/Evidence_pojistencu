class Prostredi:

    def vypis_nadpis(self):
        print(" _________________________\n   Evidence pojištěných \n _________________________\n\n")

    def vyber_akci(self):
        print("Vyberte číslo jedné z následujících akcí:\n"
                "1 - Přidat nového pojištěného\n"
                "2 - Vypsat všechny pojištěné\n"
                "3 - Vyhledat pojištěného\n"
                "4 - Ukončení aplikace\n")

    """_vycisti_obrazovku Nefunguje jak má, ale běh programu to neovlivňuje, vypíše se ? ve čtverečku"""
    def _vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.run(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call("clear")

    def zobraz_nadpis_akci(self):
        prostredi._vycisti_obrazovku()
        prostredi.vypis_nadpis()
        prostredi.vyber_akci()

    def zobraz_nadpis(self):
        prostredi._vycisti_obrazovku()
        prostredi.vypis_nadpis()

    def osetri_text_input(self, pobidka):
        while True:
            user_input = input(pobidka)
            if user_input and all((x.isalpha() or x.isspace()) for x in user_input):
                if user_input[0].isupper():
                    return user_input
                else:
                    print("První písmeno by mělo být velké.")
            else:
                print("Vstup by měl obsahovat pouze písmena a mezery.")

    def osetri_vek_input(self):
        while True:
            vek = input("Zadejte věk: ")
            if vek.isdigit():
                vek = int(vek)
                if 1 <= vek <= 120:
                    return vek
                else:
                    print("Věk by měl být v rozmezí 1 až 120 let.")
            else:
                print("Věk by měl být zadán jako číslo.")

    def osetri_telefon_input(self):
        while True:
            telefon = input("Zadejte telefon: ")
            if telefon.isdigit():
                if len(telefon) == 9:
                    return int(telefon)
                else:
                    print("Telefon by měl obsahovat devět cifer.")
            else:
                print("Telefon by měl být zadán jako číslo.")


prostredi = Prostredi()

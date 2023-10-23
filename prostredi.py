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

prostredi = Prostredi()

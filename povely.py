from prostredi import Prostredi
from databaze import Databaze

prostredi = Prostredi()
databaze = Databaze()


class Povely:
    # třída pro řízení aplikace přes volby uživatele
    def vyber_moznost(self, pokracovat = True, spatne = "Neplatná volba. Zkuste to znovu.\n"):
        while pokracovat:
            prostredi.zobraz_nadpis_akci()  # metoda vyčistí konzoli, zobrazí nadpis 'Evidence pojištěných' a zobrazí seznam voleb
            volba = int(input("Zadejte číslo úkonu: "))
            match (volba):
                case 1:
                    jmeno = prostredi.osetri_text_input("Zadejte jméno: ")          # ošetřený input od uživatele
                    prijmeni = prostredi.osetri_text_input("Zadejte příjmení: ")    # ošetřený input od uživatele
                    vek = prostredi.osetri_vek_input()                              # ošetřený input od uživatele
                    telefon = prostredi.osetri_telefon_input()                      # ošetřený input od uživatele

                    databaze.pridej_uzivatele(jmeno, prijmeni, vek,
                                              telefon)  # napojení na metodu přidávající nového pojištěného do dtb

                case 2:
                    databaze.vypis_uzivatele()          # vypíší se všichni pojištění v dtb

                case 3:
                    jmeno = prostredi.osetri_text_input("Zadejte jméno: ")          # ošetřený input od uživatele
                    prijmeni = prostredi.osetri_text_input("Zadejte příjmení: ")    # ošetřený input od uživatele

                    databaze.vyhledej_uzivatele(jmeno, prijmeni)                    # dle zadaných inputů vyhledá pojištěného z dtb

                case 4:
                    pokracovat = False                                              # ukončí se 'while' cyklus
                    databaze.ukonci_spojeni()                                       # zavření spojení s dtb
                    pass

                case _:
                    print(spatne)                                                   # špatně zadaný input pro volbu úkonu




from prostredi import Prostredi
from databaze import Databaze

prostredi = Prostredi()
databaze = Databaze()


class Povely:



    def vyber_moznost(self, pokracovat = True, spatne = "Neplatná volba. Zkuste to znovu.\n"):
        while pokracovat:
            prostredi.zobraz_nadpis_akci()
            volba = int(input("Zadejte číslo úkonu: "))
            match (volba):
                case 1:
                    jmeno = prostredi.osetri_text_input("Zadejte jméno: ")
                    prijmeni = prostredi.osetri_text_input("Zadejte příjmení: ")
                    vek = prostredi.osetri_vek_input()
                    telefon = prostredi.osetri_telefon_input()

                    databaze.pridat_uzivatele(jmeno, prijmeni, vek, telefon)

                case 2:
                    databaze.nacist_uzivatele()

                case 3:
                    jmeno = prostredi.osetri_text_input("Zadejte jméno: ")
                    prijmeni = prostredi.osetri_text_input("Zadejte příjmení: ")

                    databaze.vyhledej_uzivatele(jmeno, prijmeni)

                case 4:
                    pokracovat = False
                    databaze.ukonci_spojeni()
                    pass

                case _:
                    print(spatne)




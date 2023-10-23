from prostredi import Prostredi
from databaze import Databaze

prostredi = Prostredi()
databaze = Databaze()


class Povely:

    def vyber_moznost(self, pokracovat = True, spatne = "Nepovolená volba. Zkuste to znovu.\n"):
        while pokracovat:
            prostredi.zobraz_nadpis_akci()
            spravne_zadani = False
            while spravne_zadani != True:

                    volba = int(input("Zadejte číslo úkonu: "))
                    if volba == 1:
                        spravne_zadani = True

                        jmeno = input("Zadejte jméno: ")
                        prijmeni = input("Zadejte příjmení: ")
                        vek = int(input("Zadejte věk: "))
                        telefon = int(input("Zadejte telefonní číslo: "))

                        databaze.pridat_uzivatele(jmeno, prijmeni, vek, telefon)
                        print("Osoba byla úspěšně přidána do databáze pojištěných.")

                    elif volba == 2:
                        spravne_zadani = True

                        databaze.nacist_uzivatele()

                    elif volba == 3:
                        spravne_zadani = True

                        jmeno = input("Zadejte jméno: ")
                        prijmeni = input("Zadejte příjmení: ")

                        databaze.vyhledej_uzivatele(jmeno, prijmeni)

                    elif volba == 4:
                        spravne_zadani = True
                        pokracovat = False
                        databaze.ukonci_spojeni()
                        print("        PROGRAM UKONČEN\n------------------------------------------")
                        pass

                    else:
                        print(spatne)


povely = Povely()
povely.vyber_moznost()

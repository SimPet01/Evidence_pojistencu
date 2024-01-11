from prostredi import Prostredi
from databaze import Databaze

prostredi = Prostredi()
databaze = Databaze()


class Povely:
    """
    Třída pro řízení aplikace přes volby uživatele
    """

    def vyber_moznost(self, pokracovat = True, spatne = "Neplatná volba. Zkuste to znovu.\n"):
        """
        Provede uživatelem zvolenou operaci

        Parametry:
            :param pokracovat: Pokud je pokracovat = 'False', tak se funkce ukončí
            :param spatne: Vypíše se string pro uživatele, pokud zadá neplatnou volbu
        """
        while pokracovat:
            # metoda vyčistí konzoli, zobrazí nadpis 'Evidence pojištěných' a zobrazí seznam voleb
            prostredi.zobraz_nadpis_akci()
            # dotaz pro uživatele a zapsání jeho volby
            volba = int(input("Zadejte číslo úkonu: "))
            # provede danou volbu uživatele
            match volba:
                case 1:
                    # ošetřený input jména od uživatele
                    jmeno = prostredi.osetri_text_input("Zadejte jméno: ")
                    # ošetřený input příjmení od uživatele
                    prijmeni = prostredi.osetri_text_input("Zadejte příjmení: ")
                    # ošetřený input věku od uživatele
                    vek = prostredi.osetri_vek_input()
                    # ošetřený input telefonu od uživatele
                    telefon = prostredi.osetri_telefon_input()
                    # napojení na metodu přidávající nového pojištěného do dtb
                    databaze.pridej_uzivatele(jmeno, prijmeni, vek, telefon)

                case 2:
                    # vypíší se všichni pojištění v dtb
                    databaze.vypis_uzivatele()

                case 3:
                    # ošetřený input jména od uživatele
                    jmeno = prostredi.osetri_text_input("Zadejte jméno: ")
                    # ošetřený input příjmení od uživatele
                    prijmeni = prostredi.osetri_text_input("Zadejte příjmení: ")
                    # dle zadaných inputů vyhledá pojištěného z dtb
                    databaze.vyhledej_uzivatele(jmeno, prijmeni)

                case 4:
                    # ukončí se 'while' cyklus
                    pokracovat = False
                    # zavření spojení s dtb
                    databaze.ukonci_spojeni()
                    pass

                case _:
                    # špatně zadaný input pro volbu úkonu
                    print(spatne)

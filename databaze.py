import sqlite3
from sqlite3 import Error as SQLError


class Databaze:
    """
    Třída upravující komunikaci s databází (dtb)
    """

    def __init__(self, cur = None, conn = None):
        """
        Iniciace proměných použitých napříč metodami ve třídě Databáze

        Parametry:
            :param cur: Spojení s dtb
            :param conn: Spojení kurzory
        """
        self.cur = cur
        self.conn = conn
        self.vytvor_spojeni()
        self.vytvor_tabulku()


    def vytvor_spojeni(self, dtb_soubor = "Databáze_pojištěných"):
        """
        Vytvoří spojení s dtb

        Parametry:
            :param dtb_soubor: Název souboru dtb
        """
        try:
            self.conn = sqlite3.connect(dtb_soubor)
            self.cur = self.conn.cursor()
            return self.conn
        except SQLError:
            print("Chyba spojení s databází!\n", SQLError)


    def vytvor_tabulku(self):
        """
        Vytvoří novou tabulku (pokud již neexistuje v souboru dtb
        """
        create_table_cmd = """
        CREATE TABLE IF NOT EXISTS uzivatele (                  
            id_uzivatele INTEGER PRIMARY KEY AUTOINCREMENT,
            jmeno TEXT,
            prijmeni TEXT,
            vek INTEGER,
            telefon INTEGER)
        """
        self.cur.execute(create_table_cmd)
        self.conn.commit()


    def pridej_uzivatele(self, jmeno = "", prijmeni = "", vek = -1, telefon = -1):
        """
        Zapíše řádek s novým uživatelem do tabulky

        Parametry:
            :param jmeno: Jméno uživatele
            :param prijmeni: Příjmení uživatele
            :param vek: Věk uživatele
            :param telefon: Telefon na uživatele
        """
        # Sloupec 'id_uzivatele' si dtb vytvoří sama při každém přidání nového řádku
        insrt_cmd = "INSERT INTO uzivatele (jmeno, prijmeni, vek, telefon) VALUES(?, ?, ?, ?)"
        insrt_data = (jmeno, prijmeni, vek, telefon)
        self.cur.execute(insrt_cmd, insrt_data)
        self.conn.commit()
        print("\n------------------------------\nOsoba byla úspěšně přidána do databáze pojištěných.")


    def vypis_uzivatele(self):
        """
        Vypíše všechny v dtb uložené uživatele

        Returns:
            :return (str): Seznam v dtb uložených uživatelů
        """
        print("\n------------------------------\nV databázi jsou následující uživatelé:")
        print("(jmeno, prijmeni, vek, telefon):\n")
        self.cur.execute("SELECT jmeno, prijmeni, vek, telefon FROM uzivatele")
        vypis = self.cur.fetchall()
        if vypis:
            print("\n------------------------------\nV databázi jsou následující uživatelé:")
            print("(jmeno, prijmeni, vek, telefon):")
            for radek in vypis:
                print(radek)
            print("--------------------------\n(Konec výpisu z databáze)\n")
        else:
            print("--------------\n(DATABÁZE JE PRÁZDNÁ)\n(Konec výpisu z databáze)")


    def vyhledej_uzivatele(self, jmeno, prijmeni):
        """
        Vyhledá konkrétního uživatele

        Parametry:
            :param jmeno: Jméno uživatele
            :param prijmeni: Příjmení uživatele

        Returns:
            :return: Vyhledá jedno kontrétní jméno z dtb
        """
        self.cur.execute("SELECT jmeno, prijmeni, vek, telefon FROM uzivatele WHERE jmeno = ? AND prijmeni = ?",
                         (jmeno, prijmeni))
        vypis = self.cur.fetchall()
        if vypis:
            print("\n------------------------------\nV databázi jsou následující uživatelé:")
            print("(jmeno, prijmeni, vek, telefon):")
            for radek in vypis:
                print(radek)
            print("--------------------------\n(Konec výpisu z databáze)\n")
        else:
            print("Hledaný uživatel nebyl nalezen.")
        

    def ukonci_spojeni(self):
        """
        Ukončí spojení s dtb
        """
        self.conn.close()
        print("\n---------------------------------\n               PROGRAM UKONČEN\n---------------------------------")


databaze = Databaze()

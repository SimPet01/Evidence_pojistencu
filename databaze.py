import sqlite3
from sqlite3 import Error as SQLError

class Databaze:                                                 # třída upravující komunikaci s databází (dtb)

    def __init__(self, cur = None, conn = None):                # iniciace proměných použitých napříč metodami ve třídě Databáze
        self.cur = cur
        self.conn = conn
        self.vytvor_spojeni()
        self.vytvor_tabulku()


    def vytvor_spojeni(self, dtb_soubor = "Databáze_pojištěných",):
       try:
            self.conn = sqlite3.connect(dtb_soubor)             # vytvoření spojení s dtb
            self.cur = self.conn.cursor()                       # spojení kurzoru
            return self.conn
       except SQLError:                                         # chybová hláška
           print("Chyba spojení s databází!\n", SQLError)


    def vytvor_tabulku(self):
        create_table_cmd = """
        CREATE TABLE IF NOT EXISTS uzivatele (                  # příkaz pro dtb
            id_uzivatele INTEGER PRIMARY KEY AUTOINCREMENT,
            jmeno TEXT,
            prijmeni TEXT,
            vek INTEGER,
            telefon INTEGER)
        """
        self.cur.execute(create_table_cmd)
        self.conn.commit()


    def pridej_uzivatele(self, jmeno = "", prijmeni = "", vek = -1, telefon = -1):
        insrt_cmd = "INSERT INTO uzivatele (jmeno, prijmeni, vek, telefon) VALUES(?, ?, ?, ?)"
        insrt_data = (jmeno, prijmeni, vek, telefon)            # 'id_uzivatele' sloupec si vytvoří dtb sama při každém přidání nového řádku
        self.cur.execute(insrt_cmd, insrt_data)
        self.conn.commit()
        print("\n------------------------------\nOsoba byla úspěšně přidána do databáze pojištěných.")


    def vypis_uzivatele(self):
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
        self.conn.close()
        print("\n----------------------------------\n                PROGRAM UKONČEN\n----------------------------------")


databaze = Databaze()

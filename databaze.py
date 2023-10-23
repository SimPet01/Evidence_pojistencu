import sqlite3
from sqlite3 import Error as SQLError

class Databaze:

    def __init__(self, cur = None, conn = None):
        self.cur = cur
        self.conn = conn
        self.vytvor_spojeni()
        self.vytvor_tabulku()

    def vytvor_spojeni(self, dtb_soubor = "Databáze_pojištěných",):
       try:
            self.conn = sqlite3.connect(dtb_soubor)
            self.cur = self.conn.cursor()
            return self.conn
       except SQLError:
           print("Chyba spojení s databází!\n", SQLError)


    def vytvor_tabulku(self):
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


    def pridat_uzivatele(self, jmeno = "", prijmeni = "", vek = -1, telefon = -1):
        insrt_cmd = "INSERT INTO uzivatele (jmeno, prijmeni, vek, telefon) VALUES(?, ?, ?, ?)"
        insrt_data = (jmeno, prijmeni, vek, telefon)
        self.cur.execute(insrt_cmd, insrt_data)
        self.conn.commit()

    def nacist_uzivatele(self):
        print("\nV databázi jsou následující uživatelé:")
        print("(jmeno, prijmeni, vek, telefon)")
        self.cur.execute("SELECT jmeno, prijmeni, vek, telefon FROM uzivatele")
        for radek in self.cur.fetchall():
            print(radek)
        print("-------\n(Konec výpisu)\n")

    def vyhledej_uzivatele(self, jmeno, prijmeni):
        self.cur.execute("SELECT * FROM uzivatele WHERE jmeno = ? AND prijmeni = ?",
                   (jmeno, prijmeni))
        for radek in self.cur.fetchall():
            print(radek)

    def ukonci_spojeni(self):
        self.conn.close()


databaze = Databaze()
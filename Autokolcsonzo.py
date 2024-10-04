f = open("adatok.txt", "r")
print(f.readlines())
f.close()

from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
    
    @abstractmethod
    def leiras(self):
        pass

class Szemelyauto(Auto):
    def leiras(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap"

class Teherauto(Auto):
    def leiras(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap"

class Berles:
    def __init__(self, auto, berlo_nev, datum):
        self.auto = auto
        self.berlo_nev = berlo_nev
        self.datum = datum
    
    def leiras(self):
        return f"Bérlő: {self.berlo_nev}, Autó: {self.auto.leiras()}, Dátum: {self.datum}"

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []
    
    def auto_hozzaadasa(self, auto):
        self.autok.append(auto)
    
    def auto_berles(self, rendszam, berlo_nev, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                for berles in self.berlesek:
                    if berles.auto.rendszam == rendszam and berles.datum == datum:
                        return "Az autó már bérlés alatt van erre a napra."
                uj_berles = Berles(auto, berlo_nev, datum)
                self.berlesek.append(uj_berles)
                return f"Bérlés sikeres. Ár: {auto.berleti_dij} Ft/nap"
        return "Nincs ilyen rendszámú autó a kölcsönzőben."
    
    def berles_lemondasa(self, rendszam, berlo_nev, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.berlo_nev == berlo_nev and berles.datum == datum:
                self.berlesek.remove(berles)
                return "Bérlés sikeresen lemondva."
        return "Nincs ilyen bérlés."
    
    def berlesek_listazasa(self):
        if not self.berlesek:
            return "Nincs jelenleg aktív bérlés."
        return "\n".join([berles.leiras() for berles in self.berlesek])

def menu():
    print("\n--- Autókölcsönző Rendszer ---")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Kilépés")

def main():
    kolcsonzo = Autokolcsonzo("Példa Autókölcsönző")
    
    # Alapértelmezett autók hozzáadása
    kolcsonzo.auto_hozzaadasa(Szemelyauto("ABC-123", "Toyota Corolla", 8000))
    kolcsonzo.auto_hozzaadasa(Szemelyauto("XYZ-789", "Honda Civic", 8500))
    kolcsonzo.auto_hozzaadasa(Teherauto("AAA-111", "Ford Transit", 15000))
    
    # Például létező bérlések hozzáadása
    kolcsonzo.auto_berles("ABC-123", "Kiss János", "2024-10-01")
    kolcsonzo.auto_berles("XYZ-789", "Nagy Anna", "2024-10-02")
    kolcsonzo.auto_berles("AAA-111", "Tóth Béla", "2024-10-03")
    kolcsonzo.auto_berles("XYZ-789", "Németh Katalin", "2024-10-04")
    
    while True:
        menu()
        valasz = input("Válasszon egy opciót: ")
        
        if valasz == "1":
            rendszam = input("Adja meg az autó rendszámát: ")
            berlo_nev = input("Adja meg a nevét: ")
            datum = input("Adja meg a bérlés dátumát (YYYY-MM-DD): ")
            print(kolcsonzo.auto_berles(rendszam, berlo_nev, datum))
        
        elif valasz == "2":
            rendszam = input("Adja meg az autó rendszámát: ")
            berlo_nev = input("Adja meg a nevét: ")
            datum = input("Adja meg a bérlés dátumát (YYYY-MM-DD): ")
            print(kolcsonzo.berles_lemondasa(rendszam, berlo_nev, datum))
        
        elif valasz == "3":
            print(kolcsonzo.berlesek_listazasa())
        
        elif valasz == "4":
            print("Kilépés...")
            break
        
        else:
            print("Érvénytelen opció, próbálja újra.")

if __name__ == "__main__":
    main()














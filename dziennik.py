import json


class Dziennik:
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku
        self.uczniowie = {}

        try:
            with open(nazwa_pliku, "r") as plik:
                self.uczniowie = json.load(plik)
        except FileNotFoundError:
            pass

    def dodaj_ucznia(self, imie, nazwisko):
        dane = f"{imie} {nazwisko}"
        if dane not in self.uczniowie:
            self.uczniowie[dane] = {}
            self.zapisz_do_pliku()
            print(f"Dodano ucznia {imie} {nazwisko} do dziennika.")
        else:
            print("Uczeń już istnieje.")

    def dodaj_przedmiot(self, imie, nazwisko, przedmiot):
        dane = f"{imie} {nazwisko}"
        if dane in self.uczniowie:
            if przedmiot not in self.uczniowie[dane]:
                self.uczniowie[dane][przedmiot] = []
                self.zapisz_do_pliku()
                print(f"Dodano przedmiot {przedmiot} dla ucznia {imie} {nazwisko}.")
            else:
                print(f"Przedmiot {przedmiot} już istnieje dla ucznia {imie} {nazwisko}.")
        else:
            print("Nie ma takiego ucznia w dzienniku.")

    def dodaj_ocene(self, imie, nazwisko, przedmiot, ocena):
        dane = f"{imie} {nazwisko}"
        if dane in self.uczniowie:
            if przedmiot not in self.uczniowie[dane]:
                self.uczniowie[dane][przedmiot] = [ocena]
            else:
                self.uczniowie[dane][przedmiot].append(ocena)
            self.zapisz_do_pliku()
            print(f"Dodano ocenę {ocena} z przedmiotu {przedmiot} dla ucznia {imie} {nazwisko}.")
        else:
            print("Nie ma takiego ucznia w dzienniku.")

    def zapisz_do_pliku(self):
        with open(self.nazwa_pliku, "w") as plik:
            json.dump(self.uczniowie, plik)

    def wypisz_oceny(self, imie, nazwisko):
        dane = f"{imie} {nazwisko}"
        if dane in self.uczniowie:
            print(f"Oceny ucznia {imie} {nazwisko}:")
            for przedmiot, oceny in self.uczniowie[dane].items():
                srednia = sum(oceny) / len(oceny)
                print(f"{przedmiot}: {oceny} (średnia: {srednia:.2f})")
        else:
            print("Nie ma takiego ucznia w dzienniku.")

    def wypisz_uczniow(self):
        print("Lista uczniów w dzienniku:")
        for uczen in self.uczniowie:
            imie, nazwisko = uczen.split()
            print(f"- {imie} {nazwisko}")

if __name__ == '__main__':

    dziennik = Dziennik("dziennik.json")

    while True:
        print("Co chcesz zrobić?")
        print("1. Dodaj ucznia")
        print("2. Dodaj ocenę")
        print("3. Wyświetl oceny ucznia")
        print("4. Wyświetl liste ucznow")
        print("5. Wyjście")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            imie = input("Podaj imię ucznia: ")
            nazwisko = input("Podaj nazwisko ucznia: ")
            dziennik.dodaj_ucznia(imie, nazwisko)
            print('')
        elif wybor == "2":
            imie = input("Podaj imię ucznia: ")
            nazwisko = input("Podaj nazwisko ucznia: ")
            przedmiot = input("Podaj nazwę przedmiotu: ")
            ocena = float(input("Podaj ocenę: "))
            dziennik.dodaj_ocene(imie, nazwisko, przedmiot, ocena)
            print('')
        elif wybor == "3":
            imie = input("Podaj imię ucznia: ")
            nazwisko = input("Podaj nazwisko ucznia: ")
            dziennik.wypisz_oceny(imie, nazwisko)
            print('')
        elif wybor == "4":
            dziennik.wypisz_uczniow()
            print('')
        elif wybor == "5":
            break
        else:
            print("Niepoprawny wybór.")
            print('')

    print('-----------------------------------')



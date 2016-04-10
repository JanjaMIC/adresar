class Kontakt:
    def __init__(self):
        moja_beleznica = {}
        ime = "ime"
        priimek = "priimek"
        email = "email"
        telefon = "telefon"
        naslov = "naslov"

    def __init__(self, arg_ime, arg_priimek, arg_email, arg_telefon, arg_naslov):
        self.ime = arg_ime
        self.priimek = arg_priimek
        self.email = arg_email
        self.telefon = arg_telefon
        self.naslov = arg_naslov

    def nov_kontakt(self):
        return self.ime + self.priimek

    def uporabnikovi_podatki(self):
        return self.email + self.telefon + self.naslov


belezka = []



while True:
    odgovor = raw_input("Ali zelis dodati nov kontakt v svoj adresar (ja/ne)?")
    if odgovor == "ja":
            ime = raw_input("Vpisi ime: ")
            priimek = raw_input("Vpisi priimek: ")
            email = raw_input("Vpisi email: ")
            telefon = raw_input("Vpisi telefon: ")
            naslov = raw_input("Vpisi naslov:")
            belezka.append(ime)
            belezka.append(priimek)
            belezka.append(email)
            belezka.append(telefon)
            belezka.append(naslov)
    if odgovor == "ne":
        print "program je koncan"
        break

    print belezka







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

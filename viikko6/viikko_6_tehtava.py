# Copyright (c) 2025 Kati

from datetime import datetime, date, timedelta

def muunna_tiedot(kulutusTuotanto: list) -> list:
    
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(float(kulutusTuotanto[1].replace(",",".")))
    muutettu_tietorivi.append(float(kulutusTuotanto[2].replace(",","."))),
    muutettu_tietorivi.append(float(kulutusTuotanto[3].replace(",",".")))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> list[List]:
    kulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for kulutusTuotantoTieto in f:
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet))

    return kulutusTuotantoTiedot

def main():
    """
    Ohjelman pääfunktio: kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    kulutusTuotanto2025= lue_data("2025.csv")

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            print("Raportti aikaväliltä tulostuu...")
        elif ensimmainen_valinta == 2:
            kuukausi = input("Anna kuukauden numero (1-12): ")
            print("kuukausiraportti tulostuu...")
        elif ensimmainen_valinta == 3:
            print("Vuosiraportti tulostuu...")
        elif ensimmainen_valinta == 4:
            print("Lopetetaan ohjelma...")
            break
        else:
            continue
        
        print("---------------------------------------------------------")
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        if toinen_valinta == 1:
            print("Raportti kirjoitetaan tiedostoon...")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetetaan ohjelma...")
            break
        else:
            continue

        print("---------------------------------------------------------")

    
    #print("Valitsit", ensimmainen_valinta)
if __name__ == "__main__":
    main()
# Copyright (c) 2025 Kati

from datetime import datetime, date, timedelta
from typing import List

def muunna_tiedot(kulutusTuotanto: list) -> list:
    
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(float(kulutusTuotanto[1].replace(",",".")))
    muutettu_tietorivi.append(float(kulutusTuotanto[2].replace(",",".")))
    muutettu_tietorivi.append(float(kulutusTuotanto[3].replace(",",".")))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> List[List[float]]:
    kulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for kulutusTuotantoTieto in f:
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet))

    return kulutusTuotantoTiedot

def raportti_tiedostoon(raportti: str) -> None:
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)

def raportti_aikavali(alkupaiva: str, loppupaiva: str, tietokanta: list) -> str:
    alku = datetime.strptime(alkupaiva, "%d.%m.%Y").date()
    loppu = datetime.strptime(loppupaiva, "%d.%m.%Y").date()

    valitut = [rivi for rivi in tietokanta if alku <= rivi[0].date() <= loppu]

    if not valitut:
        return f"--- Raportti aikaväliltä {alkupaiva} - {loppupaiva} ---\nEi mittauksia."

    kulutus_summa = sum(rivi[1] for rivi in valitut)
    tuotanto_summa = sum(rivi[2] for rivi in valitut)
    keskilampo = sum(rivi[3] for rivi in valitut) / len(valitut)

    raportti = (
        f"--- Raportti aikaväliltä {alkupaiva} - {loppupaiva} ---\n"
        f"Kokonaiskulutus: {str(f'{kulutus_summa:.2f}').replace('.', ',')} kWh\n"
        f"Kokonaistuotanto: {str(f'{tuotanto_summa:.2f}').replace('.', ',')} kWh\n"
        f"Keskilämpötila: {str(f'{keskilampo:.2f}').replace('.', ',')} °C\n"
    )
    return raportti

def raportti_kuukausi(kuukausi: int, tietokanta: list) -> str:
    valitut = [rivi for rivi in tietokanta if rivi[0].month == kuukausi]

    if not valitut:
        return f"--- Kuukausiraportti {kuukausi}/2025 ---\nEi mittauksia."

    kulutus_summa = sum(rivi[1] for rivi in valitut)
    tuotanto_summa = sum(rivi[2] for rivi in valitut)
    keskilampo = sum(rivi[3] for rivi in valitut) / len(valitut)

    raportti = (
        f"--- Kuukausiraportti {kuukausi}/2025 ---\n"
        f"Kokonaiskulutus: {str(f'{kulutus_summa:.2f}').replace('.', ',')} kWh\n"
        f"Kokonaistuotanto: {str(f'{tuotanto_summa:.2f}').replace('.', ',')} kWh\n"
        f"Keskilämpötila: {str(f'{keskilampo:.2f}').replace('.', ',')} °C\n"
    )
    return raportti

def luo_vuosiraportti(data: list) -> str:
    kulutus_summa = sum(rivi[1] for rivi in data)
    tuotanto_summa = sum(rivi[2] for rivi in data)
    keskilampo = sum(rivi[3] for rivi in data) / len(data)

    raportti = (
        f"--- VUOSIRAPORTTI 2025 ---\n"
        f"Kokonaiskulutus: {str(f'{kulutus_summa:.2f}').replace('.', ',')} kWh\n"
        f"Kokonaistuotanto: {str(f'{tuotanto_summa:.2f}').replace('.', ',')} kWh\n"
        f"Keskilämpötila: {str(f'{keskilampo:.2f}').replace('.', ',')} °C\n"
    )
    return raportti

#def luo_vuosiraportti(data):
    #kokonaissumma = sum(m['kulutus'] for m in data)
    #raportti = f" --- VUOSIRAPORTTI 2025 ---\nKokonaiskulutus: {kokonaissumma:.2f} kWh\nMittauksia: {len(data)} kpl\n"
    #return raportti


def main():
    """
    Ohjelman pääfunktio: kysyy käyttäjältä inputteja ja tulostaa/vie tiedostoon raportteja
    """
    kulutusTuotanto2025= lue_data("2025.csv")
    #print(len(kulutusTuotanto2025))

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        print("---------------------")
        try:
            ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
            print("----------------")
        except ValueError:
            print("Virheellinen syöte, anna numero väliltä 1-4.")
            continue
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            print("---------------")
            raportti = raportti_aikavali(alkupaiva, loppupaiva, kulutusTuotanto2025)
            print(raportti)
        elif ensimmainen_valinta == 2:
            kuukausi = int(input("Anna kuukauden numero (1-12): "))
            raportti = raportti_kuukausi(kuukausi, kulutusTuotanto2025)
            print("kuukausiraportti tulostuu...")
            print(raportti)
        elif ensimmainen_valinta == 3:
            raportti = luo_vuosiraportti(kulutusTuotanto2025)
            print("Vuosiraportti tulostuu...")
            print(raportti)
        elif ensimmainen_valinta == 4:
            print("Lopetetaan ohjelma...")
            print("Kiitos ja hei hei!")
            break
        else:
            continue
        
        print("--------------------")
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        if toinen_valinta == 1:
            raportti_tiedostoon(raportti)
            print("Raportti kirjoitettiin tiedostoon raportti.txt..")
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
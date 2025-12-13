# Copyright (c) 2025 Kati

from datetime import datetime, date
from typing import List, Dict


def muunna_tiedot(kulutusTuotanto: list) -> list:
    
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(int(kulutusTuotanto[1]))
    muutettu_tietorivi.append(int(kulutusTuotanto[2]))
    muutettu_tietorivi.append(int(kulutusTuotanto[3]))
    muutettu_tietorivi.append(int(kulutusTuotanto[4]))
    muutettu_tietorivi.append(int(kulutusTuotanto[5]))
    muutettu_tietorivi.append(int(kulutusTuotanto[6]))
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
    
def paivantiedot(paiva: str, lukemat: list[List]) -> dict[str, list[str]]:
    pv = int(paiva.split('.')[0])
    kk = int(paiva.split('.')[1])
    vuosi = int(paiva.split('.')[2])
    
    kulutus1vaihe = 0
    kulutus2vaihe = 0
    kulutus3vaihe = 0
    tuotanto1vaihe = 0
    tuotanto2vaihe = 0
    tuotanto3vaihe = 0

    for lukema in lukemat:
        if lukema[0].date() == date(vuosi, kk, pv):
            kulutus1vaihe += lukema[1]
            kulutus2vaihe += lukema[2]
            kulutus3vaihe += lukema[3]
            tuotanto1vaihe += lukema[4]
            tuotanto2vaihe += lukema[5]
            tuotanto3vaihe += lukema[6]

   
    return {
         "kulutus": [
            f"{kulutus1vaihe/1000:.2f}".replace('.', ','),
            f"{kulutus2vaihe / 1000:.2f}".replace('.', ','),
            f"{kulutus3vaihe / 1000:.2f}".replace('.', ','),
        ],
        "tuotanto": [
            f"{tuotanto1vaihe / 1000:.2f}".replace('.', ','),
            f"{tuotanto2vaihe / 1000:.2f}".replace('.', ','),
            f"{tuotanto3vaihe / 1000:.2f}".replace('.', ',')
        ]
    }
            
#def tuntitiedot(paiva: str, lukemat: list):
    pv, kk, vuosi = map(int, paiva.split('.'))
    print(f"\nTuntikohtaiset tiedot ")
    print("Aika       Kulutus [kWh]                  Tuotanto [kWh]")
    print("           v1        v2      v3           v1       v2        v3")
    print("----------------------------------------------------------------")
    for lukema in lukemat:
        if lukema[0].date() == date(vuosi, kk, pv):
            aika = lukema[0].strftime("%H:%M")
            print(f"{aika:<6} "
                  f"{lukema[1]/1000:8.2f}".replace('.', ','),
                  f"{lukema[2]/1000:8.2f}".replace('.', ','),
                  f"{lukema[3]/1000:8.2f}".replace('.', ','),
                  f"{lukema[4]/1000:12.2f}".replace('.', ','),
                  f"{lukema[5]/1000:8.2f}".replace('.', ','),
                  f"{lukema[6]/1000:8.2f}".replace('.', ','))
    print()

def muodosta_rivi(viikonpaiva: str, paiva_str: str, yhteenveto: Dict[str, List[str]]) -> str:
    return (f"{viikonpaiva:<12} {paiva_str:<10} "
            f"{yhteenveto['kulutus'][0]:>6} {yhteenveto['kulutus'][1]:>7} {yhteenveto['kulutus'][2]:>7} "
            f"{yhteenveto['tuotanto'][0]:>9} {yhteenveto['tuotanto'][1]:>7} {yhteenveto['tuotanto'][2]:>7}")
    
def kirjoita_raportti(viikot: Dict[str, tuple], tiedoston_nimi: str) -> None:
    viikonpaivat = ["maanantai", "tiistai", "keskiviikko",
                    "torstai", "perjantai", "lauantai", "sunnuntai"]
    
def main():
    viikko41 = lue_data("viikko41.csv")
    viikko42 = lue_data("viikko42.csv")
    viikko43 = lue_data("viikko43.csv")
    
    viikot = {
        "Viikko 41": (viikko41, ["06.10.2025","07.10.2025","08.10.2025","09.10.2025","10.10.2025","11.10.2025","12.10.2025"]),
        "Viikko 42": (viikko42, ["13.10.2025","14.10.2025","15.10.2025","16.10.2025","17.10.2025","18.10.2025","19.10.2025"]),
        "Viikko 43": (viikko43, ["20.10.2025","21.10.2025","22.10.2025","23.10.2025","24.10.2025","25.10.2025","26.10.2025"])
    }
              
    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko",
                "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    
    kirjoita_raportti(viikot, "yhteenveto.txt")
  
     
    for viikkonimi, (lukemat, paivat) in viikot.items():
        print(f"\n{viikkonimi}")
        print("Viikon sähkökulutus ja -tuotanto (kWh, päivän kokonaiskulutus ja tuotanto)", end="\n")
        print("Päivä        Pvm         Kulutus [kWh]              Tuotanto [kWh]")
        print("                         v1      v2      v3         v1      v2      v3")
        print("---------------------------------------------------------------------------")
        for pvm in paivat:
            pv, kk, vuosi = map(int, pvm.split('.'))
            paiva_obj = datetime(vuosi, kk, pv)
            viikonpaiva = viikonpaivat[paiva_obj.weekday()]

            yhteenveto = paivantiedot(pvm, lukemat)
            print(f"{viikonpaiva:<12} {pvm:<10} "
              f"{yhteenveto['kulutus'][0]:>6} {yhteenveto['kulutus'][1]:>7} {yhteenveto['kulutus'][2]:>7} "
              f"{yhteenveto['tuotanto'][0]:>9} {yhteenveto['tuotanto'][1]:>7} {yhteenveto['tuotanto'][2]:>7}")
            if viikonpaiva == "Sunnuntai":
                print("---------------------------------------------------------------------------")
    

if __name__ == "__main__":
    main()
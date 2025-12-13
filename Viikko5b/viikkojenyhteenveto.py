from datetime import datetime, date


def muunna_tiedot(kulutusTuotanto: list) -> list:
    """Muuttaa jokaisen annetun tietorivin tietotyypin oikeiksi"""
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutusTuotanto[0]))
    muutettu_tietorivi.append(int(kulutusTuotanto[1]))
    muutettu_tietorivi.append(int(kulutusTuotanto[2]))
    muutettu_tietorivi.append(int(kulutusTuotanto[3]))
    muutettu_tietorivi.append(int(kulutusTuotanto[4]))
    muutettu_tietorivi.append(int(kulutusTuotanto[5]))
    muutettu_tietorivi.append(int(kulutusTuotanto[6]))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> list:
    
    kulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for kulutusTuotantoTieto in f:
            varaus = kulutusTuotantoTieto.strip()
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusTuotantoTiedot.append(muunna_tiedot(kulutusTuotantoTietoSarakkeet))
    return kulutusTuotantoTiedot
    
def paivantiedot(paiva: str, lukemat: list) -> int:
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
        "kulutus": (kulutus1vaihe + kulutus2vaihe + kulutus3vaihe) / 1000, 
        "tuotanto": (tuotanto1vaihe + tuotanto2vaihe + tuotanto3vaihe ) / 1000
    }
            
def tuntitiedot(paiva: str, lukemat: list):
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


def main():
    lukemat = lue_data("viikko41.csv")
    
    print("Viikon 41 sähkökulutus ja -tuotanto (kWh, tunneittain)", end="\n")
    print(lue_data("viikko41.csv")[0][0])
    print()
    
    
    paivat = ["06.10.2025","07.10.2025","08.10.2025","09.10.2025","10.10.2025","11.10.2025","12.10.2025"]            
    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko",
                "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]


    for  pvm in paivat:
        pv, kk, vuosi = map(int, pvm.split('.'))
        paiva_obj = datetime(vuosi, kk, pv)
        viikonpaiva = viikonpaivat[paiva_obj.weekday()]
        
     
        print(".....................................................................")
        print(f"{viikonpaiva:<12} {pvm:<12}")
              
        tuntitiedot(pvm, lukemat)
        yhteenveto = paivantiedot(pvm, lukemat)
        print(f"Päivän kokonaiskulutus: {yhteenveto['kulutus']:.2f} kWh")
        print(f"Päivän kokonaistuotanto: {yhteenveto['tuotanto']:.2f} kWh\n")


if __name__ == "__main__":
    main()
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
    #hinta = float(varaus[7])
    #hinta_str = f"{hinta:.2f}".replace(".", ",")
    #muutettu_varaus.append(hinta_str)
    #muutettu_varaus.append(varaus[8].lower() == "true")
    #muutettu_varaus.append(varaus[9])
    #muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y %H:%M"))
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
    lasketutTiedot = []
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

    lasketutTiedot.append(kulutus1vaihe/1000)
    lasketutTiedot.append(kulutus2vaihe/1000)
    lasketutTiedot.append(kulutus3vaihe/1000)
    lasketutTiedot.append(tuotanto1vaihe/1000)
    lasketutTiedot.append(tuotanto2vaihe/1000)
    lasketutTiedot.append(tuotanto3vaihe/1000)
    return lasketutTiedot
            
def tuntitiedot(paiva: str, lukemat: list):
    pv, kk, vuosi = map(int, paiva.split('.'))
    print(f"\nTuntikohtaiset tiedot {paiva}")
    print("Aika     Kulutus [kWh]                Tuotanto [kWh]")
    print("         v1      v2      v3            v1     v2     v3")
    print("-------------------------------------------------------")
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


def main():
    lukemat = lue_data("viikko42.csv")
    #print(lue_data("viikko42.csv"))
    #print(lue_data("viikko42.csv")[1][0])
    print("Viikon 42 sähkökulutus ja -tuotanto (kWh, vaiheittain)", end="\n")
    print(lue_data("viikko42.csv")[0][0])
    print()
    print("Päivä          Pvm          Kulutus [kWh]                 Tuotanto [kWh]")
    print("              (pv.kk.vvvv)  v1      v2      v3            v1     v2     v3")
    print("---------------------------------------------------------------------------")
    maanantainlukemat = paivantiedot("13.10.2025", lukemat)
    print(f"Maanantai       13.10.2025", f"{maanantainlukemat[0]:6.2f}".replace('.',','), end="")
    print(f"{maanantainlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{maanantainlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{maanantainlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{maanantainlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{maanantainlukemat[5]:6.2f}".replace('.',','),)
    maanantainlukemat = paivantiedot("13.10.2025", lukemat)
    print("...päivän summat...")
    tuntitiedot("13.10.2025", lukemat)

    
    tiistainlukemat = paivantiedot("14.10.2025", lukemat)
    print(f"Tiistai         14.10.2025", f"{tiistainlukemat[0]:6.2f}".replace('.',','), end="" )
    print( f"{tiistainlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{tiistainlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{tiistainlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{tiistainlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{tiistainlukemat[5]:6.2f}".replace('.',','),)
    tiistainlukematlukemat = paivantiedot("13.10.2025", lukemat)
    print("...päivän summat...")
    tuntitiedot("14.10.2025", lukemat)

    keskiviikonlukemat = paivantiedot("15.10.2025", lukemat)
    print(f"Keskiviikko     15.10.2025", f"{keskiviikonlukemat[0]:6.2f}".replace('.',','), end= "")
    print( f"{keskiviikonlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{keskiviikonlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{keskiviikonlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{keskiviikonlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{keskiviikonlukemat[5]:6.2f}".replace('.',','),)
    print("...päivän summat...")
    tuntitiedot("15.10.2025", lukemat)

    torstainlukemat = paivantiedot("16.10.2025", lukemat)
    print(f"Torstai         16.10.2025", f"{torstainlukemat[0]:6.2f}".replace('.',','), end= "")
    print( f"{torstainlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{torstainlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{torstainlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{torstainlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{torstainlukemat[5]:6.2f}".replace('.',','),)
    print("...päivän summat...")
    tuntitiedot("16.10.2025", lukemat)

    perjantainlukemat = paivantiedot("17.10.2025", lukemat)
    print(f"Perjantai       17.10.2025", f"{perjantainlukemat[0]:6.2f}".replace('.',','), end= "")
    print( f"{perjantainlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{perjantainlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{perjantainlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{perjantainlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{perjantainlukemat[5]:6.2f}".replace('.',','),)
    print("...päivän summat...")
    tuntitiedot("17.10.2025", lukemat)

    lauantainlukemat = paivantiedot("18.10.2025", lukemat)
    print(f"Lauantai        18.10.2025", f"{lauantainlukemat[0]:6.2f}".replace('.',','), end= "")
    print( f"{lauantainlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{lauantainlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{lauantainlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{lauantainlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{lauantainlukemat[5]:6.2f}".replace('.',','),)
    print("...päivän summat...")
    tuntitiedot("18.10.2025", lukemat)

    sunnuntainlukemat = paivantiedot("19.10.2025", lukemat)
    print(f"Sunnuntai       19.10.2025", f"{sunnuntainlukemat[0]:6.2f}".replace('.',','), end= "")
    print( f"{sunnuntainlukemat[1]:6.2f}".replace('.',','), end= "\t")
    print(f"{sunnuntainlukemat[2]:6.2f}".replace('.',','), end= "\t\t")
    print(f"{sunnuntainlukemat[3]:6.2f}".replace('.',','), end= "\t")
    print(f"{sunnuntainlukemat[4]:6.2f}".replace('.',','), end= "\t")
    print(f"{sunnuntainlukemat[5]:6.2f}".replace('.',','),)
    print("...päivän summat...")
    tuntitiedot("19.10.2025", lukemat)

if __name__ == "__main__":
    main
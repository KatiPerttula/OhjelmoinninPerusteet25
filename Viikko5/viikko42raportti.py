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

    #lasketutTiedot.append(kulutus1vaihe/1000)
    #lasketutTiedot.append(kulutus2vaihe/1000)
    #lasketutTiedot.append(kulutus3vaihe/1000)
   #lasketutTiedot.append(tuotanto1vaihe/1000)
    #lasketutTiedot.append(tuotanto2vaihe/1000)
    #lasketutTiedot.append(tuotanto3vaihe/1000)
    return lasketutTiedot
            
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
    lukemat = lue_data("viikko42.csv")
    #print("Viikon 42 sähkökulutus ja -tuotanto (kWh, vaiheittain)", end="\n")
    print("Viikon 42 sähkökulutus ja -tuotanto (kWh, tunneittain)", end="\n")
    print(lue_data("viikko42.csv")[0][0])
    print()
    
    
    paivat = ["13.10.2025","14.10.2025","15.10.2025","16.10.2025","17.10.2025","18.10.2025","19.10.2025"]            
    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko",
                "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]


    for  pvm in paivat:
        pv, kk, vuosi = map(int, pvm.split('.'))
        paiva_obj = datetime(vuosi, kk, pv)
        viikonpaiva = viikonpaivat[paiva_obj.weekday()]
        
        #print("---------------------------------------------------------------------------")
        #print("Päivä      Pvm            Kulutus [kWh]                 Tuotanto [kWh]")
        #print("           (pv.kk.vvvv)   v1      v2   v3            v1     v2     v3")
        print(".....................................................................")
        print(f"{viikonpaiva:<12} {pvm:<12}")
        

        #lukemat_pv = paivantiedot(pvm, lukemat)
        #print(f"{nimi:<12} {pvm:<12} "
          #f"{lukemat_pv[0]:8.2f}".replace('.', ','),
         #f"{lukemat_pv[1]:8.2f}".replace('.', ','),
         # f"{lukemat_pv[2]:8.2f}".replace('.', ','),
          #f"{lukemat_pv[3]:12.2f}".replace('.', ','),
          #f"{lukemat_pv[4]:8.2f}".replace('.', ','),
          #f"{lukemat_pv[5]:8.2f}".replace('.', ','))
        tuntitiedot(pvm, lukemat)


if __name__ == "__main__":
    main ()
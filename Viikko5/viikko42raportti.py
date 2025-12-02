
def lue_data(tiedoston_nimi: str) -> list:
    
    kulutusTuotantoTiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        for kulutusTuotantoTieto in f:
            varaus = kulutusTuotantoTieto.strip()
            kulutusTuotantoTieto = kulutusTuotantoTieto.strip()
            kulutusTuotantoTietoSarakkeet = kulutusTuotantoTieto.split(';')
            kulutusTuotantoTiedot.append(kulutusTuotantoTietoSarakkeet)
    return kulutusTuotantoTiedot
    

def main():
    print(lue_data("viikko42.csv"))



if __name__ == "__main__":
    main()
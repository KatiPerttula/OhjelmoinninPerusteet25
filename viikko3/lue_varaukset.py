from datetime import datetime, timedelta

def hae_varausnumero(varaus): #-> INT: ...
    return int(varaus[0])
def hae_varaaja(varaus):
    return str(varaus[1])
def hae_paiva(varaus):
    return datetime.strptime(varaus[2], "%Y-%m-%d").date()
def hae_aloitusaika(varaus):
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
    aika = datetime.strptime(varaus[3], "%H:%M").time()
    return datetime.combine(paiva, aika)
def hae_Tuntimaara(varaus):
    return float(varaus[4])
def hae_Tuntihinta(varaus):
    return float(varaus[5])
def laske_kokonaishinta(varaus):
    Tuntimäärä = float(varaus[4])
    Tuntihinta = float(varaus[5])
    return Tuntimäärä * Tuntihinta
def hae_maksettu(varaus): # -> bool ...
    return (varaus[6].lower()) == "true"
def hae_kohde(varaus):
    return str(varaus[7])
def hae_puhelin(varaus):
    return str(varaus[8])
def hae_sahkoposti(varaus):
    return str(varaus[9])

def tulosta_varaus(varaus):
    Varausnumero = hae_varausnumero(varaus)
    Varaaja = hae_varaaja(varaus)

    paiva = hae_paiva(varaus)
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus[3], "%H:%M").time()
    suomalainenAika = aika.strftime("%H.%M")

    Tuntimäärä = hae_Tuntimaara(varaus)
    Tuntihinta = hae_Tuntihinta(varaus)
    Tuntihinta_str = f"{Tuntihinta:.2f}".replace(".", ",")
    Kokonaishinta = laske_kokonaishinta(varaus)
    Kokonaishinta_str = f"{Kokonaishinta:.2f}".replace(".", ",")
    Maksettu = hae_maksettu(varaus)
    Varauskohde = hae_kohde(varaus)
    Puhelinnumero = hae_puhelin(varaus)
    Sähköposti = hae_sahkoposti(varaus)          
              
    print(f"Varausnumero: {Varausnumero}")
    print(f"Varaaja: {Varaaja}")
    print(f"Päivämäärä: {suomalainenPaiva}")
    print(f"Aloitusaika: {suomalainenAika}")
    print(f"Tuntimäärä: {Tuntimäärä}")
    print(f"Tuntihinta: {Tuntihinta_str} €")
    print(f"Kokonaishinta: {Kokonaishinta_str} €")
    print(f"Maksettu: {'Kyllä' if Maksettu else 'Ei'}")
    print(f"Varauskohde: {Varauskohde}")
    print(f"Puhelinnumero: {Puhelinnumero}")
    print(f"Sähköposti: {Sähköposti}")
    print("-")

def main():
    varaukset = "varaukset.txt"
        
    with open(varaukset, "r", encoding="utf-8") as f:
        for rivi in f:
            varaus = rivi.strip().split("|")
            tulosta_varaus(varaus)
            
            
            #Nope
if __name__ == "__main__":
    main()


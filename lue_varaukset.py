from datetime import datetime, timedelta

def main():
    varaukset = "varaukset.txt"
    Yhteishinta = 0.0

    with open(varaukset, "r", encoding="utf-8") as f:
        for rivi in f:
            varaus = rivi.strip().split("|")
            
            Varausnumero = int(varaus[0])
            Varaaja = str(varaus[1])

            paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
            suomalainenPaiva = paiva.strftime("%d.%m.%Y")
            aika = datetime.strptime(varaus[3], "%H:%M").time()
            suomalainenAika = aika.strftime("%H.%M")

            Tuntimäärä = float(varaus[4])
            Tuntihinta = float(varaus[5])
            Tuntihinta_str = f"{Tuntihinta:.2f}".replace(".", ",")
            Kokonaishinta = Tuntimäärä * Tuntihinta
            Kokonaishinta_str = f"{Kokonaishinta:.2f}".replace(".", ",")
            Maksettu = bool(varaus[6].lower())== "true"
            Varauskohde = str(varaus[7])
            Puhelinnumero = str(varaus[8])
            Sähköposti = str(varaus[9])
            Aloitus = datetime.combine(paiva, aika)
            Loppumisaika = Aloitus + timedelta(hours=Tuntimäärä)

            Kokonaishinta = Tuntimäärä * Tuntihinta
            Yhteishinta += Kokonaishinta
            Yhteishinta_str = f"{Yhteishinta:.2f}".replace(".", ",")

            print(f"Varausnumero:{Varausnumero}")
            print(f"Varaaja:{Varaaja}")
            print(f"Tuntimäärä:{Tuntimäärä}")
            print(f"Tuntihinta:{Tuntihinta_str} €")
            print(f"Päivämäärä:{suomalainenPaiva}")
            print(f"Aloitusaika:{suomalainenAika}")
            print(f"Kokonaishinta:{Kokonaishinta_str} €")
            print(f"Maksettu: {'Kyllä' if Maksettu else 'Ei'}")
            print(f"Varauskohde:{Varauskohde}")
            print(f"Puhelinnumero:{Puhelinnumero}")
            print(f"Sähköposti:{Sähköposti}")
            print(f"Loppumisaika:{Loppumisaika.strftime('%d.%m.%Y %H.%M')}")
            print("-")

    print(f"Kaikkien varauksien yhteishinta: {Yhteishinta_str} €")
    
if __name__ == "__main__":
    main()


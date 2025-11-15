def main():
    varaukset = "varaukset.txt"
    Yhteishinta = 0.0
    
    with open(varaukset, "r", encoding="utf-8") as f:
        for rivi in f:
            varaus = rivi.strip().split("|")
            
            Varausnumero = hae_varausnumero(varaus)
            Varaaja = hae_varaaja(varaus)

            paiva = hae_paiva(varaus)
            suomalainenPaiva = paiva.strftime("%d.%m.%Y")
            aika = datetime.strptime(varaus[3], "%H:%M").time()
            suomalainenAika = aika.strftime("%H.%M")

            Tuntimäärä = hae_tuntimaara(varaus)
            Tuntihinta = hae_tuntihinta(varaus)
            Tuntihinta_str = f"{Tuntihinta:.2f}".replace(".", ",")
            Kokonaishinta = laske_kokonaishinta(varaus)
            Kokonaishinta_str = f"{Kokonaishinta:.2f}".replace(".", ",")
            Maksettu = hae_maksettu(varaus)
            Varauskohde = hae_kohde(varaus)
            Puhelinnumero = hae_puhelin(varaus)
            Sähköposti = hae_sahkoposti(varaus)
                       
            Yhteishinta += Kokonaishinta

            Aloitus = hae_aloitusaika(varaus)
            Loppumisaika = Aloitus + timedelta(hours=Tuntimäärä)

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
            print(f"Loppumisaika: {Loppumisaika.strftime('%d.%m.%Y %H.%M')}")
            print("-")
        
    Yhteishinta_str = f"{Yhteishinta:.2f}".replace(".", ",")
    print(f"Kaikkien varauksien yhteishinta: {Yhteishinta_str} €")

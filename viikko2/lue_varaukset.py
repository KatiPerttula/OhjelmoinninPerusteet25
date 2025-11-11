def main():
    
    varaukset = "varaukset.txt"

    
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    varaus = varaus.split('|')

    from datetime import datetime
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus[3], "%H:%M").time()
    suomalainenAika = aika.strftime("%H.%M")

    

    Varausnumero = int(varaus[0])
    Varaaja = str(varaus[1])
    #Varauspäivä = datetime.date(varaus[2])
    #aloitusaika = datetime.time(varaus[3])
    Tuntimäärä = float(varaus[4])
    Tuntihinta = float(varaus[5])
    #Tuntihinta_str = f"{Tuntihinta:.2f}".replace(".", ",")
    Kokonaishinta = Tuntimäärä * Tuntihinta
    Maksettu = bool(varaus[6])
    Varauskohde = str(varaus[7])
    Puhelinnumero = str(varaus[8])
    Sähköposti = str (varaus[9])

   

    print(f"Varausnumero:{Varausnumero}")
    print(f"Varaaja:{Varaaja}")
    print(f"Tuntimäärä:{Tuntimäärä}")
    print(f"Tuntihinta:{Tuntihinta}")
    print(f"Päivämäärä:{suomalainenPaiva}")
    print(f"Aloitusaika:{suomalainenAika}")
    print(f"Kokonaishinta: {float(varaus[4]) * float(varaus[5]):.2f} €") 
        #print(f"Maksettu:{Maksettu}")
    print(f"Maksettu: {'Kyllä' if Maksettu else 'Ei'}")
    print(f"Varauskohde:{Varauskohde}")
    print(f"Puhelinnumero:{Puhelinnumero}")
    print(f"Sähköposti:{Sähköposti}")
    print("-" * 40)  # erotin rivien väliin
   
 
  

if __name__ == "__main__":
    main()
def main():
    varaukset = "varaukset.txt"

    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
    print(varaus)

if __name__ == "__main__":
    main()

Varausnumero = int(varaus[0])
Varaaja = str(varaus[1])
Päivämäärä = datetime(varaus[2])
Aloitusaika = datetime.time(varaus[3])
Tuntimäärä = int(varaus[4])
Tuntihinta = float(varaus[5])
Kokonaishinta = float(varaus[6]) == "True"
Maksettu = bool(varaus(7))
Kohde = str(varaus[8])
Puhelin = str(varaus[9])
Sähköposti = str(varaus[10])

print(f"Varausnumero:{Varausnumero}")



        
    
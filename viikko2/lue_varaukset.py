import datetime


def main():
    varaukset = "varaukset.txt"
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        print(varaus)

varaus = varaus.split('|')

varausnumero = int(varaus[0])
varaaja = str(varaus[1])
varauspäivä = datetime.date(varaus[2])
aloitusaika = datetime.time(varaus[3])
tuntimäärä = int(varaus[4])
tuntihinta = float(varaus[5])
maksettu = bool(varaus[6])
varauskohde = str(varaus[7])
puhelinnumero = str(varaus[8])
sähköposti = str (varaus[9])

if __name__ == "__main__":
    main()

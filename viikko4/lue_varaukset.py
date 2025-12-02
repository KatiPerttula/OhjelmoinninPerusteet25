from datetime import datetime, date, time

def muunna_varaustiedot(varaus: list) -> list:

    muutettu_varaus = []

    muutettu_varaus.append(int(varaus[0]))
    muutettu_varaus.append(varaus[1])
    muutettu_varaus.append(varaus[2])
    muutettu_varaus.append(varaus[3])
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").strftime("%d.%m.%Y"))
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").strftime("%H:%M"))
    muutettu_varaus.append(int(varaus[6]))
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append(varaus[8].lower() == "true")
    muutettu_varaus.append(varaus[9])
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y %H:%M"))
    return muutettu_varaus

def hae_varaukset(varaustiedosto: str) -> list:
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            varaustiedot = rivi.split("|")
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def main():
    varaukset = hae_varaukset("varaukset.txt")
    for varaus in varaukset:
        print("|".join(str(x) for x in varaus))


if __name__ == "__main__":
    main()
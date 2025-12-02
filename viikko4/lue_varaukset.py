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

    #muutettu_varaus.append(float(varaus[7])).replace(".", ",")
    hinta = float(varaus[7])
    hinta_str = f"{hinta:.2f}".replace(".", ",")
    muutettu_varaus.append(hinta_str)

    muutettu_varaus.append(varaus[8].lower() == "true")
    muutettu_varaus.append(varaus[9])
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y %H:%M"))
    return muutettu_varaus

def hae_varaukset(varaustiedosto: str) -> list:
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split("|")
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistut_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        #print (" Nimi, Varattu tila, pv.kk.vvvv klo hh.mm")
        if (varaus[8]):
            print(f"- {varaus[1]}, {varaus[9]}, {varaus[4]} klo: {varaus[5]}")

    print()

def pitkät_varaukset(varaukset: list):
       # - Nimi, pv.kk.vvvv klo hh.mm, kesto X h, Varattu tila
    for varaus in varaukset[1:]:
        if (varaus[6]) >= 3:
            print(f"- {varaus[1]}, {varaus[4]} klo: {varaus[5]}, kesto: {varaus[6]} h, {varaus[9]}")

    print()

def varausten_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        if (varaus[8]):
            print(f"- {varaus[1]} → Vahvistettu")
        else: 
            print(f"- {varaus[1]} → Ei vahvistettu")

    print()

def varausten_määrä(varaukset: list):
    vahvistetutVaraukset = 0
    eiVahvistetutvaraukset = 0
    for varaus in varaukset[1:]:
        if (varaus[8]):
            vahvistetutVaraukset += 1
        else: 
            eiVahvistetutvaraukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {eiVahvistetutvaraukset} kpl")

    print()

def varausten_kokonaistulot(varaukset: list):
    varaustenTulot = 0
    for varaus in varaukset[1:]:
        varaustenTulot += float(varaus[7].replace(",", "."))
             
    print(f"Vahvistettujen varausten kokonaistulo: {varaustenTulot} €")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset:")
    vahvistut_varaukset(varaukset)

    print("2) Pitkät varaukset (≥ 3 h):")
    pitkät_varaukset(varaukset)

    print("3) Varausten vahvistusstatus:")
    varausten_vahvistusstatus(varaukset)

    print("4) Yhteenveto vahvistuksista:")
    varausten_määrä(varaukset)

    print("5) Vahvistettujen varausten kokonaistulot:")
    varausten_kokonaistulot(varaukset)

   

 #   print("------------------------------------------------------------------------")
 #   for varaus in varaukset:
 #       print(" | ".join(str(x) for x in varaus))
 #       print("------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
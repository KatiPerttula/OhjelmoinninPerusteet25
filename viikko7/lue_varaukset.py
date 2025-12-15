# Copyright (c) 2025 Kati Perttula


from datetime import datetime

def muunna_varaustiedot(varaus_lista: list[str]) -> dict:
    return {
        "id": int(varaus_lista[0]),
        "nimi": varaus_lista[1],
        "sähköposti": varaus_lista[2],
        "puhelin": varaus_lista[3],
        "varauksenPvm": datetime.strptime(varaus_lista[4],"%Y-%m-%d").date(),
        "varauksenKlo": datetime.strptime(varaus_lista[5], "%H:%M").time(),
        "varauksenKesto": int(varaus_lista[6]),
        "hinta": float(varaus_lista[7]),
        "varausVahvistettu": varaus_lista[8].lower() == "true",
        "varattuTila": varaus_lista[9],
        "varausLuotu": datetime.strptime(varaus_lista[10],"%Y-%m-%d %H:%M:%S"),
    }

def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            varaustiedot = rivi.strip().split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: list[dict]):
    for varaus in varaukset[1:]:
        if varaus["varausVahvistettu"]:
            print(f"- {varaus['nimi']}, {varaus['varattuTila']}, {varaus['varauksenPvm'].strftime('%d.%m.%Y')} klo {varaus['varauksenKlo'].strftime('%H.%M')}")
    print()

def pitkat_varaukset(varaukset: list[dict]):
    for varaus in varaukset[1:]:
        if(varaus["varauksenKesto"] >= 3):
            print(f"- {varaus['nimi']}, {varaus['varauksenPvm'].strftime('%d.%m.%Y')} klo {varaus['varauksenKlo'].strftime('%H.%M')}, kesto {varaus['varauksenKesto']} h, {varaus['varattuTila']}")
    print()

def varausten_vahvistusstatus(varaukset: list[dict]):
    for varaus in varaukset[1:]:
        status = "Vahvistettu" if varaus["varausVahvistettu"] else "EI vahvistettu"
        print(f"{varaus['nimi']} → {status}")
    print()

def varausten_lkm(varaukset: list[dict]):
    vahvistetut = sum(1 for v in varaukset if v["varausVahvistettu"])
    ei_vahvistetut = len(varaukset) - vahvistetut
    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-Vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: list[dict]):
    tulot = sum(v["varauksenKesto"] * v["hinta"] for v in varaukset if v["varausVahvistettu"])
    print("Vahvistettujen varausten kokonaistulot:", f"{tulot:.2f}".replace('.', ','), "€")
    print()
    
def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()
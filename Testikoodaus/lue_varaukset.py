# Copyright (c) 2025 Kati Perttula
#olio versio
from datetime import datetime

class Varaus:
    def __init__(self, varaus_lista: list[str]):
        self.id = int(varaus_lista[0])
        self.nimi = varaus_lista[1]
        self.sähköposti = varaus_lista[2]
        self.puhelin = varaus_lista[3]
        self.varauksenPvm = datetime.strptime(varaus_lista[4], "%Y-%m-%d").date()
        self.varauksenKlo = datetime.strptime(varaus_lista[5], "%H:%M").time()
        self.varauksenKesto = int(varaus_lista[6])
        self.hinta = float(varaus_lista[7])
        self.varausVahvistettu = varaus_lista[8].lower() == "true"
        self.varattuTila = varaus_lista[9]
        self.varausLuotu = datetime.strptime(varaus_lista[10], "%Y-%m-%d %H:%M:%S")

    def on_vahvistettu(self) -> bool:
        return self.varausVahvistettu

    def on_pitka(self) -> bool:
        return self.varauksenKesto >= 3

    def tulot(self) -> float:
        return self.varauksenKesto * self.hinta if self.varausVahvistettu else 0.0

    def __str__(self):
        return f"{self.nimi}, {self.varattuTila}, {self.varauksenPvm.strftime('%d.%m.%Y')} klo {self.varauksenKlo.strftime('%H.%M')}"

class VarausHallinta:
    def __init__(self, tiedosto: str):
        self.varaukset = self._lataa_varaukset(tiedosto)

    def _lataa_varaukset(self, tiedosto: str) -> list[Varaus]:
        varaukset = []
        with open(tiedosto, "r", encoding="utf-8") as f:
            for rivi in f:
                varaustiedot = rivi.strip().split('|')
                varaukset.append(Varaus(varaustiedot))
        return varaukset

    def vahvistetut_varaukset(self):
        for v in self.varaukset:
            if v.on_vahvistettu():
                print("-", v)
        print()

    def pitkat_varaukset(self):
        for v in self.varaukset:
            if v.on_pitka():
                print(f"- {v}, kesto {v.varauksenKesto} h")
        print()

    def vahvistusstatus(self):
        for v in self.varaukset:
            status = "Vahvistettu" if v.on_vahvistettu() else "EI vahvistettu"
            print(f"{v.nimi} → {status}")
        print()

    def yhteenveto(self):
        vahvistetut = sum(1 for v in self.varaukset if v.on_vahvistettu())
        ei_vahvistetut = len(self.varaukset) - vahvistetut
        print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
        print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
        print()

    def kokonaistulot(self):
        tulot = sum(v.tulot() for v in self.varaukset)
        print("Vahvistettujen varausten kokonaistulot:", f"{tulot:.2f}".replace('.', ','), "€")
        print()

def main():
    hallinta = VarausHallinta("varaukset.txt")
    print("1) Vahvistetut varaukset")
    hallinta.vahvistetut_varaukset()
    print("2) Pitkät varaukset (≥ 3 h)")
    hallinta.pitkat_varaukset()
    print("3) Varausten vahvistusstatus")
    hallinta.vahvistusstatus()
    print("4) Yhteenveto vahvistuksista")
    hallinta.yhteenveto()
    print("5) Vahvistettujen varausten kokonaistulot")
    hallinta.kokonaistulot()

if __name__ == "__main__":
    main()
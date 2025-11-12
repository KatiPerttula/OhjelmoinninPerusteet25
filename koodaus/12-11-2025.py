def ekafunktio():
    print("Tämä on eka funktio")

def tokafuntio(kurssi="", numero=0):
    #sana = "lisätään " + sana
    print(f"{kurssi}, arvosana {numero}")
    print(kurssi, "arvosana", numero)
    print(kurssi, end=" ")
    print("arvosana", end=" ")
    print(numero)

def kolmasfunktio(etunimi="Mikko", sukunimi = "Mallikas"):
    """Tämä palauttaa jotain"""
    return etunimi +" " + sukunimi

def neljasfunktio():
    return "Jippiii"

def leikkialistankanssa():
    teksti = "opiskelija;ohjelmoija;kehittäjä"
    sanat = teksti.split(";")
    print(sanat[0])
    sanat =(teksti.split(";")[0])

def main():
    #print("Yahoo")
    #ekafunktio()
    #tokafuntio("Ohjelmoinnin perusteet", 5)
    #kolmannenpalautus = kolmasfunktio("Matti", "Meikäläinen")
    #print(kolmannenpalautus)
    #print(kolmasfunktio())
    #print(neljasfunktio())
    leikkialistankanssa()

if __name__ == "__main__":
    main()

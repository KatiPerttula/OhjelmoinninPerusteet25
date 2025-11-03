def main():
    varaukset = "varaukset.txt"
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        print(varaus)


        
    
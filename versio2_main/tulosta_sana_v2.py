def main():
    tiedosto = "sana.txt"
    with open(tiedosto, "r", encoding="utf-8") as f:
        sana = f.read().strip()
        print(sana)

if__name__== "__main__": # type: ignore
main()
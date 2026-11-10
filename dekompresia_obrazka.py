def spracuj_riadok(riadok):
    cisla = riadok.split()
    vys = ""
    for i in range(len(cisla)):
        pocet = int(cisla[i])
        if i % 2 == 0:
            vys += "0" * pocet
        else:
            vys += "1" * pocet
    return vys


with open("dekompresia_obrazka_1.txt", "r") as fr:
    a, b = fr.readline().split()
    roz = int(a) * int(b)
    print(f"{a},{b} - počet pixelov: {roz}")
    riadky = [r.strip() for r in fr if r.strip()]

print(spracuj_riadok(riadky[0]))

with open("dekompresia_obrazka_vystup.txt", "w") as fw:
    fw.write(f"{a} {b}\n")
    for riadok in riadky:
        fw.write(spracuj_riadok(riadok) + "\n")
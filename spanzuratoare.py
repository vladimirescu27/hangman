id_student = "Tocaciu Vladut"
litere =['A', 'E', 'I', 'O', 'U', 'Ă', 'Î', 'Ȃ', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'Z', 'Ș', 'Ț', 'X']
jocuri = []

def adaugalitere(litera, cuvant, pozitii_litere):
    cuvantnou = list(cuvant)
    for pozitie in pozitii_litere:
        cuvantnou[pozitie] = litera
    cuvantnou = "".join(cuvantnou)
    cuvant = cuvantnou
    return cuvant


def unde_se_potriveste_litera(id_student, id_joc, litera):
    pozitiilitere = []
    for joc in jocuri:
        if joc["id"] == id_joc:
            cuvantcorect = joc["cuvantcorect"]
            joc["incercari"] +=1
    for i in range(0, len(cuvantcorect)):
        if cuvantcorect[i] == litera:
            pozitiilitere.append(i)
    return pozitiilitere

def rezolva(joc):
    i=0
    id = joc["id"]
    cuvantcompus = joc["cuvant"]
    while "*" in cuvantcompus:
        if i < len(litere):
            pozitiilitere = unde_se_potriveste_litera(id_student,id,litere[i])
            cuvantcompus = adaugalitere(litere[i], cuvantcompus, pozitiilitere)
            i += 1
        else:
            break

def verifica_cuvantul(id_student, id_joc, cuvant_format):
    for joc in jocuri:
        if joc["id"] == id_joc:
            cuvantcorect = joc["cuvantcorect"]
    if cuvant_format ==cuvantcorect:
        return 1
    else:
        return 0

def main():
    nrjoc = 0
    numarTotalIncercari = 0
    with open("cuvinte_de_verificat.txt", "r",) as f:
        for linie in f.readlines():
            linie = linie.split(";")
            nrjoc += 1
            id = linie[0]
            cuvant = linie[1]
            cuvantcorect = linie[2].replace("\n","")
            incercari = 0
            jocuri.append({"id": id, "cuvant":cuvant, "cuvantcorect":cuvantcorect, "incercari": incercari})
    for joc in jocuri:
        rezolva(joc)
    print("Numar jocuri: ", nrjoc)
    for joc in jocuri:
        numarTotalIncercari += joc["incercari"]
    print("Incercari: ", numarTotalIncercari)
    with open("date_iesire_timestamp.txt", "w") as g:
        for joc in jocuri:
            print(joc["id"], ";", joc["incercari"], sep="")
            g.write(str(str(joc["id"])+";"+str(joc["incercari"])+"\n"))




if __name__ == '__main__':
    main()
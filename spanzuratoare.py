import hangmanClient, json


id_student = "vlad_olimpiu10@yahoo.com"
password = "PFQVUN"
hangmanClient.login(id_student, password)
litere =['A', 'E', 'I', 'O', 'U', 'Ă', 'Î', 'Ȃ', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'Z', 'Ș', 'X']
jocuri = []

# Functia care gaseste litera.
def adaugalitere(litera, cuvant, pozitii_litere):
    cuvantnou = list(cuvant)
    for pozitie in pozitii_litere:
        cuvantnou[pozitie] = litera
    cuvantnou = "".join(cuvantnou)
    cuvant = cuvantnou
    return cuvant


# Functia care gaseste pozitia unde se potriveste litera.
def rezolva(joc):
    i=0
    id = joc["id"]
    cuvantcompus = joc["cuvant"]
    while "*" in cuvantcompus:
        if i < len(litere):
            pozitiilitere = unde_se_potriveste_litera(id_student,id,litere[i])
            cuvantcompus = adaugalitere(litere[i], cuvantcompus, pozitiilitere)
            i = i+1
        else:
            break
        verifica_cuvantul(id_student,id,cuvantcompus)

# Functia care gaseste pozitia literei si o salveaza intr-o lista unde se potriveste aceasta.
def unde_se_potriveste_litera(id_student, id_joc, litera):
    '''''''''
    pozitiilitere = []
    for joc in jocuri:
        if joc["id"] == id_joc:
            cuvantcorect = joc["cuvantcorect"]
            joc["incercari"] = joc["incercari"] + 1
    for i in range(0, len(cuvantcorect)):
        if cuvantcorect[i] == litera:
            pozitiilitere.append(i)
    return pozitiilitere
    '''''
    for joc in jocuri:
        if joc["id"] == id_joc:
            joc["incercari"] +=1
        return hangmanClient.check_letter(id_joc, litera)


# Functia care verifica daca cuvantul este unul corect sau nu.
def verifica_cuvantul(id_student, id_joc, cuvant_format):
    ''''for joc in jocuri:
        if joc["id"] == id_joc:
            cuvantcorect = joc["cuvantcorect"]
    if cuvant_format ==cuvantcorect:
        return 1
    else:
        return 0
        '''''
    return hangmanClient.check_word(id_joc, cuvant_format)

def main():
    nrjoc = 0
    numarTotalIncercari = 0

    while True:
        game = hangmanClient.new_game()
        game = {"id": game["game_id"], "cuvant": game["word_to_guess"], "cuvantcorect": "", "incercari": 0}
        nrjoc += 1
        if game["id"] == 100:
            break
        jocuri.append(game)

    for joc in jocuri:
        rezolva(joc)

    print("Numar jocuri: ", nrjoc)
    for joc in jocuri:
        numarTotalIncercari = numarTotalIncercari + joc["incercari"]
    print("Incercari: ", numarTotalIncercari)
    with open("date_iesire_timestamp.txt", "w", encoding="utf-8") as g:
        for joc in jocuri:
            print(joc["id"], ";", joc["incercari"], sep="")
            g.write(str(str(joc["id"])+";"+str(joc["incercari"])+"\n"))


if __name__ == '__main__':
    main()

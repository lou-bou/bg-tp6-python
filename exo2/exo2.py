# liste de dicts (slides 31, 32)
C = [
    {"nom": "compte1", "solde": 1000},
    {"nom": "compte2", "solde": 500},
    {"nom": "compte3", "solde": 3000}
]


# fonction typée (slides 40, 41)
def deposer(c: dict, somme: float) -> dict:
    if somme <= 0:  # if (slide 35)
        return {"erreur": "montant invalide"}
    c["solde"] += somme
    return {"compte": c["nom"], "solde": c["solde"]}


def retirer(c: dict, somme: float) -> dict:
    if somme <= 0:  # if / elif (slide 35)
        return {"erreur": "montant invalide"}
    elif somme > c["solde"]:
        return {"erreur": "solde insuffisant"}
    c["solde"] -= somme
    return {"compte": c["nom"], "solde": c["solde"]}


def afficher(c: list) -> dict:
    total = 0
    for compte in c:  # boucle for (slide 38)
        total += compte["solde"]
    print(f"solde total: {total}")  # f-string (slide 55)
    return {"total": total}


def filtre1000(c: list) -> list:
    resultat = []
    for compte in c:  # boucle for (slide 38)
        if compte["solde"] >= 1000:
            resultat.append({"compte": compte["nom"], "solde": compte["solde"]})  # append (slide 27)
    return resultat


# trie en prenant le plus grand solde à chaque tour
def trier(c: list) -> list:
    reste = c.copy()  # copy (slide 27)
    resultat = []
    while len(reste) > 0:  # boucle while (slide 22)
        plus_grand = reste[0]
        for compte in reste:
            if compte["solde"] > plus_grand["solde"]:
                plus_grand = compte
        reste.remove(plus_grand)  # remove (slide 27)
        resultat.append({"compte": plus_grand["nom"], "solde": plus_grand["solde"]})
    return resultat


# point d'entrée (slide 55)
if __name__ == "__main__":
    print(deposer(C[0], 500))
    print(deposer(C[0], -50))
    print(retirer(C[1], 200))
    print(retirer(C[1], 9999))
    print(afficher(C))
    print(filtre1000(C))
    print(trier(C))

# liste de tuples (slides 26, 28)
students = [
    (1000, "JOHN", "DOE", 14, 5),
    (2000, "BOB", "CARLTON", 7, 1),
    (3000, "RAYANE", "SMITH", 13, 3)
]


# fonction typée (slides 40, 41), retourne une liste de dicts (slide 32)
def A(students: list) -> list:
    resultats = []
    for student in students:  # boucle for (slide 38)
        mat = student[0]  # index du tuple (slide 28)
        if B(student[3]):  # if / else (slide 35)
            result = "ADMIS"
        else:
            result = "AJOURNE"
        resultats.append({'mat': mat, 'result': result})  # dict + append (slides 31, 27)
    return resultats


# prend un float, retourne un bool (slide 41), comparaison >= (slide 34)
def B(note: float) -> bool:
    return note >= 10


# appelle B et affiche les résultats
def C():
    for student in students:  # boucle for (slide 38)
        mat = student[0]
        if B(student[3]):  # if / else (slide 35)
            result = "ADMIS"
        else:
            result = "AJOURNE"
        print(f"{mat}: {result}")  # f-string (slide 55)


# point d'entrée (slide 55)
if __name__ == "__main__":
    C()

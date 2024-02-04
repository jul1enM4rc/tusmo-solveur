from wordbase import *
import random as rd
import numpy as np
from tqdm import tqdm
import statistics

file = r"dataframe.csv"

score_juste = 2
score_presque = 1

lettres = "abcdefghijklmnopqrstuvwxyz"

sample = [
    "tour",
    "emoi",
    "joli",
    "amok",
    "fion",
    "toum"
]

fl = "r"


def get_score(mot, guess, motCount=None):
    taille = len(mot)
    score = [0] * taille
    if motCount is None:
        motCount = {lettre: mot.count(lettre) for lettre in lettres}
    guessCount = {lettre: 0 for lettre in lettres}
    for i in range(taille):
        if mot[i] == guess[i]:
            score[i] = score_juste
            guessCount[guess[i]] += 1
        elif guess[i] in mot and guessCount[guess[i]] < motCount[guess[i]]:
            guessCount[guess[i]] += 1
            score[i] = score_presque
    return score


def jouer(taille):
    df = list(get_base(file, taille))

    mot_cache = rd.choice(df)
    mot_devine = ""

    print(mot_cache[0] + "".join(["_"] * taille))

    while mot_devine != mot_cache:
        mot_devine = input("nouveau guess :")
        print(get_score(mot_cache, mot_devine))


def enlever_mot(ancien, conditions, liste):
    liste_remove = [0] * len(liste)
    taille = len(ancien)
    for i in range(len(liste)):
        mot = liste[i]
        for j in range(taille):
            lettre = mot[j]
            lanc = ancien[j]
            if conditions[j] == 2 and lanc != lettre:
                liste_remove[i] = 1
                break
            elif conditions[j] == 1 and ((lanc not in mot) or (lanc == lettre)):
                liste_remove[i] = 1
                break
            elif conditions[j] == 0 and (
                    mot.count(lanc) > sum([1 for t, x in enumerate(ancien) if ((x == lanc) and (conditions[t] > 0))])):
                liste_remove[i] = 1
                break
    liste_new = []
    for i in range(len(liste)):
        if liste_remove[i] == 0:
            liste_new.append(liste[i])
    print(liste_new)
    return liste_new


def get_proposal(liste_totale, liste_possible):
    L = len(liste_totale)
    l = len(liste_possible)


    tableau = np.full([L, l], np.nan)

    for x in tqdm(range(L), desc='Progress'):
        motCount = {lettre: liste_totale[x].count(lettre) for lettre in lettres}
        for y in range(l):
            val = sum(get_score(liste_totale[x], liste_possible[y], motCount))
            tableau[x][y] = val

    tableau /= len(liste_totale[0]) * score_juste
    moyennes = np.mean(tableau, axis=1)
    index = np.argmax(moyennes)
    print(moyennes)
    print(moyennes[index])
    return liste_totale[index]


def main():
    fl = input("première lettre : ")
    taille = int(input('taille : '))
    liste_mot = get_base(file, taille, fl)
    liste_possible =liste_mot.copy()
    results = [0]
    while statistics.mean(results) != 2:
        prop = get_proposal(liste_mot, liste_possible)
        print(prop)
        results = input("resultats : ")

        results = [int(char) for char in results]

        liste_possible = enlever_mot(prop, results, liste_possible)
        if prop in liste_possible:
            liste_possible.remove(prop)


if __name__ == "__main__":
    main()

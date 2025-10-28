import csv 
r={"a", "a", 23}

with open("data/songs.csv", "r" ) as f:
    cs= csv.DictReader(f, delimiter=",")
    for ligne in cs:
        print(ligne)



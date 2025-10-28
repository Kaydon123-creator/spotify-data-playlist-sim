
class AgeTropPetitErreur(Exception):
    pass
class NomdejaLaErreur(Exception):
    pass

class CourrielmauvaisError(Exception):
    pass
def f(l_d):
    dic={}
    for nom, courriel, age in l_d:
        if age < 18:
            raise AgeTropPetitErreur("ooooo") 
        if nom in dic:
            raise NomdejaLaErreur 
        if len(courriel.split("@"))!= 2:
            raise CourrielmauvaisError 
        dic[nom]=(courriel, age) 
    return dic
try:
    a=f([("alice", "alice@example.com", 10),
    ("bob", "bob@example.com", 95), 
    ("carol", "carole@xample.com", 25),  
    ("alie", "alice2@example.com", 30), 
    ("dave", "dave@example.com", 35)])
    print(a)
except AgeTropPetitErreur as e:
    print(f"age trop petit {e}")

except NomdejaLaErreur:
    print("Nom déjà là")
except CourrielmauvaisError:
    print("mauvais courriel")

from sooso import a as e
print(e(2))
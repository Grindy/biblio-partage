bibliotheque = []

#ajout d'un livre en dictionnaire dans la liste bibliotheque
def ajouter_livre(titre, auteur):
    bibliotheque.append({"titre": titre, "auteur":auteur})

#test d'ajouter livre
ajouter_livre("Harry Potter", "JK Rowling")
print(bibliotheque)

def afficher_livres():
    pass

def rechercher_livre(titre):
    pass
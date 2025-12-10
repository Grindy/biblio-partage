bibliotheque = []
short = "-" * 50

#ajout d'un livre en dictionnaire dans la liste bibliotheque
def ajouter_livre(titre, auteur):
    bibliotheque.append({"titre": titre, "auteur":auteur})

#test d'ajouter livre
ajouter_livre("Harry Potter", "JK Rowling")
print(bibliotheque)

# Affichage du contenu de la bibliotheque
def afficher_livres():
    print(f"{short}\nVoici le contenu de ma biblio :\n")
    for livre in list(bibliotheque):
        print("•", livre["titre"], "écrit par", livre["auteur"])

#test affichage du contenu de la bibliotheque
afficher_livres()

def rechercher_livre(titre):
    
    print("\nRésultats trouvés : \n")

    compteur = 1
    for livre in bibliotheque:
        if livre['titre'].lower() == titre.lower():
            info_livre = f"{livre['titre']} par {livre['auteur']}"
            print(f"{compteur}. {info_livre}")
            compteur += 1

# test rechercher_livre (MAD)
rechercher_livre("Harry Potter")
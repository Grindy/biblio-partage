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
        print("\nRésultats trouvés : \n")

        compteur = 1
        for livre in bibliotheque:
            if livre['titre'].lower() == titre.lower():
                info_livre = f"{livre['titre']} par {livre['auteur']}"
                print(f"{compteur}. {info_livre}")
                compteur += 1
                  

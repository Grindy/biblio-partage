bibliotheque = [
    {"titre": "L'écume des jours", "auteur": "Boris Vian"},
    {"titre": "Mémoires d'un Boomer", "auteur": "Marc-André Dufour"},
    {"titre": "Candide", "auteur": "Voltaire"}
    ]

short = "-" * 50

# Affichage du contenu de la bibliotheque
def afficher_livres():
    print(f"\nVoici le contenu de ma biblio :\n")
    for livre in list(bibliotheque):
        print("•", livre["titre"], "de", livre["auteur"],)

# #test affichage du contenu de la bibliotheque
afficher_livres()

#ajout d'un livre en dictionnaire dans la liste bibliotheque
def ajouter_livre(titre, auteur):
    bibliotheque.append({"titre": titre, "auteur":auteur})
    print(f"\nLe livre {titre} de {auteur} a bien été ajouté à la bibliothèque!")

# #test d'ajouter livre
ajouter_livre("Harry Potter", "JK Rowling")

## test d'affichage après un ajout
afficher_livres()

print(f"\n{short}")

def rechercher_livre(titre):

    print(f"\nRecherche de: {titre}\n.\n.\n.")
    
    print("\nRésultats trouvés : \n")

    compteur = 1
    for livre in bibliotheque:
        if livre['titre'].lower() == titre.lower():
            info_livre = f"{livre['titre']} par {livre['auteur']}"
            print(f"{compteur}. {info_livre}")
            compteur += 1

## test rechercher_livre (MAD)
rechercher_livre("Harry Potter")
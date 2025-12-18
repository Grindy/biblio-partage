from biblio_partage import bibliotheque, afficher_livres, ajouter_livre, rechercher_livre

# Tests fait avec module Pytest Runner


def test_TrouverLivres():
    assert bibliotheque[0] == {"titre": "L'écume des jours", "auteur": "Boris Vian"}
    assert bibliotheque[1] == {"titre": "Mémoires d'un Boomer", "auteur": "Marc-André Dufour"}
    assert bibliotheque[2] == {"titre": "Candide", "auteur": "Voltaire"}
    assert bibliotheque[3] == {"titre": "Harry Potter", "auteur": "JK Rowling"}

def test_AfficherLivres():
    for livre in list(bibliotheque):
        assert "L'écume des jours" == bibliotheque[0]["titre"] and "Boris Vian" == bibliotheque[0]["auteur"]
        assert "Mémoires d'un Boomer" == bibliotheque[1]["titre"] and "Marc-André Dufour" == bibliotheque[1]["auteur"]
        assert "Candide" == bibliotheque[2]["titre"] and "Voltaire" == bibliotheque[2]["auteur"]
        assert "Harry Potter" == bibliotheque[3]["titre"] and "JK Rowling" == bibliotheque[3]["auteur"]

def test_RechercherLivre():
    assert rechercher_livre('Harry Potter') == None
    assert rechercher_livre('Candide') == None

# test_RechercherLivre a revoir!
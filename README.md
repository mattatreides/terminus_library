# Sujet:

Dans le cadre de la modernisation de son système d'information, la bibliothèque municipale vous demande de concevoir un système de gestion de son stock de livres. Afin de pouvoir gérer correctement cette bibliothèque, les utilisateurs du système doivent pouvoir : 

    Ajouter, Modifier et Supprimer les auteurs

    Ajouter, Modifier et Supprimer les livres

    Gérer les emprunts de livres et le stock de livres


L’utilisation de l’application se fera via une API REST que vous implémenterez en suivant les best-practices.

Pour cet exercice aucune programmation HTML/CSS/JS n’est attendue, le système doit pouvoir se reposer entièrement sur les capacités de l’API pour administrer les différents composants de la bibliothèque.

En plus du code source Python 3, vous fournirez un dump de la base de données permettant de tester l’application, ainsi qu’un schéma UML au format png/jpeg justifiant l’implémentation de l'application proposée.

Bonus : 

    Fournir un fichier docker-compose et ses fichiers dépendants avec votre code source permettant le test et le déploiement rapide de votre application et des différents composants.

    Endpoint de recherche d’un livre

    Gestion de l’authentification


# terminus_library

ORM: SQLALchemy

Framework web: FastAPI

BDD: Postgres 

## start with:

```docker build -t terminus . ```

```docker compose up srv```

## TODO:
- [X] ops (install env)
- [X] Connexion sqlalchemy <-> postgres
- [X] definition et creation du model de la BDD
- [X] créer api /book/
- [x] discover fastapi & sqlalchemy
- [] créer api /author/
- [] créer api /loan/
- [] livrables: shema UML & dump bdd
- [] créer api recherche de livre

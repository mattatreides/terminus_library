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

**ORM**: SQLALchemy

**Framework web**: FastAPI

**BDD**: Postgres

### How it works 
*Build docker image:*
`docker build . --no-cache -t terminus`

*run the server*
`*docker-compose up*`

*(The database is create automaticly, default name as terminus_bookcase)

*Connect to DB*
`docker exec -it terminus_library-db-1 psql -U tech terminus_bookcase`

*Delete database:*
`docker exec -it terminus_library-db-1 psql -U tech -c 'DROP DATABASE terminus_bookcase;'`

*Init demo data*
`scripts/init\_demo\_data.sh`

*Get Books*:
`curl http://localhost:88/books/ | json_pp`

*Add Author*
```
curl -d \
  '{"id": 1, 
    "name":"Asimov", 
    "firstname": "Isaac", 
    "country": "US"}' \
  -H "Content-Type: application/json" -X \
  POST http://localhost:88/author/

```

*Add Book*
```
curl -d \
  '{"id": 1,
    "title":"fondation",
    "description": "livre de SF",
    "author_id": 1,
    "author": "Isaac Asimov"}' \
  -H "Content-Type: application/json" -X \
  POST http://localhost:88/book/
```


## TODO:
- [X] ops (install env)
- [X] Connexion sqlalchemy <-> postgres
- [X] definition et creation du model de la BDD
- [X] créer api /book/
- [x] discover fastapi & sqlalchemy
- [x] créer api /author/
- [ ] créer api /loan/
- [ ] livrables: shema UML & dump bdd
- [ ] créer api recherche de livre

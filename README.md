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

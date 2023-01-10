#!/bin/bash
curl -d   '{"id": 1, "name":"Asimov", "firstname": "Isaac", "country": "US"}'   -H "Content-Type: application/json" -X   POST http://localhost:88/author/
curl -d   '{"id": 1,"title":"Fondation 1","description": "livre de SF","author_id": 1,"author": "Isaac Asimov"}'   -H "Content-Type: application/json" -X   POST http://localhost:88/book/
curl -d   '{"id": 2 ,"title":"Robots 1","description": "livre de SF","author_id": 1,"author": "Isaac Asimov"}'   -H "Content-Type: application/json" -X   POST http://localhost:88/book/
curl -d   '{"id": 3 ,"title":"le robot qui revait","description": "livre de SF","author_id": 1,"author": "Isaac Asimov"}'   -H "Content-Type: application/json" -X   POST http://localhost:88/book/
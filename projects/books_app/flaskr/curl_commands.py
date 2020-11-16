# GET the / endpoint
curl http://172.18.0.2:3000/

# GET the /books end point
curl http://172.18.0.2:3000/books

# GET the /books end point for id=2
curl -X GET http://172.18.0.2:3000/books/2

# Use key value pair to GET page 2 via pagination
curl -X GET http://172.18.0.2:3000/books?page=2

# PATCH the /books end point for id=2 with a rating of 1, from another previously recorded value of 5
curl http://172.18.0.2:3000/books/2 -X PATCH -H "Content-Type : application/json" -d '{"rating": "1"}'

# DELETE the /books end point for id=2
curl -X DETELE http://172.18.0.2:3000/books/2

# POST a new book
curl -X POST -H "Content-Type : application/json" -d '{"title": "Neverwhere", "author": "Neil Gaimen", "rating": "5"}' http://172.18.0.2:3000/books
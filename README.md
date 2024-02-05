# Mobile Network



## How to run the project

make sure you have docker and docker-compose.
then run

```bash 
docker-compose up --build
```

## How to enjoy the project

access [localhost:8000/?q=20+boulevard+des+italiens+75008+Paris]()


## App workflow

- Get address for query parameters
- ask https://api-adresse.data.gouv.fr/ with the address
- get first result properties x and y, in lambert93 according to documentation
- get rows in CSV that are closest to this x and y by euclidian distance
- Get one row per Operateur from the result
- discard results that are too far from the actual x and y (500 meters)
- format the output based on the results
- serve it


## Design choices

> premature optimization is the root of all evil 

No need to over-engineer the project. 

- FastAPI does the job, so could have Flask or even SimpleHTTPServer
- With the current data access system, it is similar to a database for which we open close connection instead of keeping it open, it's fine
- about Classes: I disagree with [Stop writing classes](https://youtu.be/o9pEzgHorH0?si=QU2EeOyTduHFQ5jB&t=1043). We can discuss it

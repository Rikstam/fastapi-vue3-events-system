## General
Run and build the app, run 
`docker compose up -d --build` in the project root.

## Backend

Run migrations
`docker compose exec events-backend aerich upgrade`

Run tests
`docker compose exec events-backend python -m pytest -v`
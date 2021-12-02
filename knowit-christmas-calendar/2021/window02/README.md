# window02

```bash
docker run --name santa-postgis --volume $(pwd):/tmp -e POSTGRES_PASSWORD=anything -d ghcr.io/baosystems/postgis:14-3.1
docker exec -ti santa-postgis psql -U postgres -a -f "/tmp/window02.sql"
docker container stop santa-postgis
docker container rm santa-postgis
```

# docker-compose up -d --build

# # make sure the postgres container is ready, then run migrations
# sleep 5
# docker exec dog_park-api-1 python /src/manage.py makemigrations 
# docker exec dog_park-api-1 python /src/manage.py migrate
COMPOSE_DOCKER_CLI_BUILD=0 DOCKER_BUILDKIT=0 docker-compose up -d
sleep 10
docker exec dog_park-api-1 python manage.py migrate
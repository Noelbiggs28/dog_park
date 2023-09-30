docker-compose up -d --build

# make sure the postgres container is ready, then run migrations
sleep 5
docker exec dog_park_api-1 python /src/manage.py makemigrations 
docker exec dog_park_api-1 python /src/manage.py migrate
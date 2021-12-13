# debian-feeder

To test the debian-feeder, it is easier using the docker-compose deployment:

```
git clone git@github.com:fasten-project/fasten-docker-deployment.git
cd fasten-docker-deployment/
docker-compose --profile c up -d
```

Then, cloning and compiling:

```
cd 
git clone git@github.com:endocode/debian-feeder.git
sudo apt-get install libpq-dev
sudo apt-get update -y
sudo apt-get install -y python3-psycopg2
cd debian-feeder
python3 debian_feeder.py
```

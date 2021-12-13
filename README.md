# debian-feeder

To test the debian-feeder, it is easier to use the docker-compose deployment:

First install docker-compose:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version
```

and docker:

```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
sudo usermod -aG docker ${USER}
```

Clone the `fasten-docker-deployment` repository:

```
git clone git@github.com:fasten-project/fasten-docker-deployment.git
cd fasten-docker-deployment/
docker-compose --profile c up -d
```

Then, clone and compile the debian-feeder:

```
cd 
git clone git@github.com:endocode/debian-feeder.git
sudo apt-get install -y libpq-dev
sudo apt-get update -y
sudo apt-get install -y python3-psycopg2
cd debian-feeder
python3 debian_feeder.py
```

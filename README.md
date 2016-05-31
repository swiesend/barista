# Barista

This is the famous Barista service.

You can order:

|Coffee|Price*|
|----|----|
|Americano|1.50€
|Cappuccino|2.00€
|Espresso|1.30€
|Latte Macchiato|2.20€
|Moccaccino|2.30€

* prices change according to their preparation process

# Getting Started
This is an example flask webserver with docker and python3.

To start the service make sure to have docker installed.

**build** a docker image:

    git clone https://github.com/swiesend/barista barista
    cd barista
    docker build -t barista .

**run** it in a container on port 5000:

    docker run -d -p 5000:5000 barista

# Configuration

    This webserver configuration is not for production use!

For production use a configuration which might be more like this:

https://realpython.com/blog/python/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/

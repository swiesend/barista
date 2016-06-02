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



**install** docker, if you don't have it yet:

    https://docs.docker.com/linux/step_one/

**build** a docker image, which will contain the whole webserver:

    git clone https://github.com/swiesend/barista barista
    cd barista
    docker build -t barista .

**run** it in a docker container on port 5000:

    docker run -d -p 5000:5000 barista

**use** use the app in your favorite browser:

    http://localhost:5000

# Configuration

    This webserver configuration is not for production use!

For production use a configuration which might be more like this:

https://realpython.com/blog/python/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/


# Issues

## [todo] Setup a post-receive hook for Jenkins with GitHub plugin

ok, let's setup a hook:

* go to the repository `Settings`
* click `Webhooks & services` on the left
* click `Add service` button
* type `Jenkins (GitHub plugin)``
* enter the following url to Jenkins hook url

    http://78.46.74.23:8080/github-webhook/


you should see something like this as response on the top:


    Okay, that hook was successfully created.

done!

## [bug] Missing 'Latte Macchiato'

Oh, no the 'Latte Macchiato' is missing. A customer has raised an issue to this topic. Please fix the problem.

**check** the coffee module to find a solution:

    barista/coffee.py

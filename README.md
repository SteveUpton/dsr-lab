#### 1. Build and run the rongen service

The rongen service is a HTTP api for getting Ron Swanson quotes. It also publishes the same quote using zeromq when it gets a request.

In the rongen directory:

`docker build -t rongen .`

`docker run --name rg -p 5000:5000 -p 4444:4444 -t rongen`

#### 2. Build and run the frontend

The frontend gets quotes from the rongen service and bolds them for the user.

In the frontend directory:

`docker build -t frontend .`

`docker run --name fe --link rg:rongen -p 5001:5001 -t frontend`

#### 2. Build and run the ronlog service

The ronlog service logs every time a message is published by the rongen service, along with the time.

In the ronlog directory:

`docker build -t ronlog .`

`docker run --name rl --link rg:rongen -p 5002:5002 -t ronlog`

#### Credits

Ron Swanson quotes from [jamesseanwright/ron-swanson-quotes](https://github.com/jamesseanwright/ron-swanson-quotes).

Forked from [original example here](http://blog.apcelent.com/how-to-setup-microservices-python-zeromq-docker-example.html).

Some Flask stuff from [containertutorials.com](http://containertutorials.com/docker-compose/flask-simple-app.html).

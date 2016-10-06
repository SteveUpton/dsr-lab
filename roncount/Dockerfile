FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y --force-yes python python-dev python-setuptools software-properties-common gcc python-pip
RUN apt-get clean all

RUN pip install pyzmq
RUN pip install Flask

# Flask Port
EXPOSE 5002

# Zmq Sub Server
EXPOSE 4444

COPY . /app
WORKDIR /app
RUN mkdir /app/static

CMD python logger.py & python printer.py

FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install Flask
RUN pip install requests

ENTRYPOINT ["python"]
CMD ["app.py"]

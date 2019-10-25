FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3-dev python3-pip

RUN apt-get install -y bash

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["main.py"]
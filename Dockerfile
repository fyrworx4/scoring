FROM ubuntu:latest
COPY . /opt/app
WORKDIR /opt/app
RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install -r requirements.txt
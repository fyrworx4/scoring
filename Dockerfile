FROM ubuntu:latest
COPY . /opt/app
WORKDIR /opt/app
RUN apt-get update && apt-get install -y \
    python3-pip
RUN python3 -m pip install -r requirements.txt
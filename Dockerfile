FROM ubuntu:latest
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
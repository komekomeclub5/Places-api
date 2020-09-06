FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask
RUN pip3 install urllib
RUN pip3 install -U googlemaps --user

RUN mkdir /app
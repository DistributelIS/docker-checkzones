FROM debian:latest
MAINTAINER Denis Lemire <denis.lemire@distributel.ca>

USER root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install -y bind9utils python3

COPY checkzones.py /checkzones.py

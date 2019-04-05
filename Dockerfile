FROM debian:latest
MAINTAINER Razvan Crainea <razvan@opensips.org>

USER root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install -y bind9utils python3

COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]

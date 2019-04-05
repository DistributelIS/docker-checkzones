FROM debian:jessie
MAINTAINER Razvan Crainea <razvan@opensips.org>

USER root
ENV DEBIAN_FRONTEND noninteractive
ARG VERSION=2.4

RUN apt-get update -qq && apt-get install -y bind9utils

COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]

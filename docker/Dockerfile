FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt -y install python3 \
                   python3-dev \
				   python3-pip \
				   libcairo2-dev \
				   pkg-config
				   
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install pycairo
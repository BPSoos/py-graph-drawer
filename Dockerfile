FROM alpine:3.14

RUN apk add bash
RUN apk add python3-tkinter
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN python -m pip install graphics.py

RUN echo '#!/bin/bash' > ~/.bashrc;echo 'alias ll='"'"'ls -alF'"'"'' >> ~/.bashrc

COPY . /root/Graphs/
FROM ubuntu:18.04

LABEL maintainer="Benjamin Seiler <bbseiler@stanford.edu>"

## General settings
ENV LANG C.UTF-8

## Python etc.
RUN apt-get update && apt-get install -y \
    git \
    curl \
    python3 \
    python3-pip

RUN python3 -m pip --no-cache-dir install --upgrade \
    "pip<20.3" \
    setuptools

## ML packages
RUN python3 -m pip install --no-cache-dir \
     numpy pandas scipy requests

## Jupyer Notebook
RUN python3 -m pip install --no-cache-dir jupyter

RUN mkdir -p /opt && cd /opt \
    && git clone https://github.com/cohortshapley/uniquenessshapley  \
    && pip install -e uniquenessshapley
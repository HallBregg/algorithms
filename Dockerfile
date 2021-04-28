FROM python:3.9
RUN apt-get update && apt-get -y upgrade
RUN pip install pytest
ENV PYTHONPATH=/
WORKDIR /algorithms
COPY ./algorithms .
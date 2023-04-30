FROM python:latest

RUN mkdir -p usr/src/app

COPY . usr/src/app

WORKDIR . usr/src/app

ENTRYPOINT ["python", "binomialoptionspricing/binomialoptionspricing.py"]
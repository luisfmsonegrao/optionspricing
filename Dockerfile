FROM python:3.10-bullseye

RUN mkdir -p usr/src/app

COPY . usr/src/app

WORKDIR /usr/src/app

ENTRYPOINT ["python", "binomialoptionspricing/binomialoptionpricing.py"]
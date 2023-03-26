FROM 3.10.10-alpine3.17

RUN mkdir -p usr/src/app

COPY . usr/src/app

WORKDIR . usr/src/app

ENTRYPOINT ["python", "binomialoptionspricing/binomialoptionspricing.py"]
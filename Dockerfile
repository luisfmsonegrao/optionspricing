FROM python:3.10-bullseye

RUN mkdir -p usr/src/app~
RUN pip install --no-cache-dir numpy

COPY ./binomialoptionspricing usr/src/app

WORKDIR /usr/src/app

ENTRYPOINT ["pytest", "binomialoptionspricing/test.py"]
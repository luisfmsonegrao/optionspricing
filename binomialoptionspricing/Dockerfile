FROM python:3.10-slim-bullseye

RUN pip install numpy

RUN mkdir /usr/src/binomialoptionspricing

COPY . /usr/src/binomialoptionspricing

WORKDIR /usr/src/binomialoptionspricing

CMD ["python", "-m", "unittest", "binomialoptionpricing.py"] 

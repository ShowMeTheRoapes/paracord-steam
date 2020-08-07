FROM python:3.7-alpine

COPY . ./uats
WORKDIR /uats

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python3 -m unittest discover -s ./tests -p '*uat.py'"]
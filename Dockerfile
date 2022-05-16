# syntax=docker/dockerfile:1

FROM python:3.6

WORKDIR /nate-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "python3", "-m" , "gunicorn", "-b", "0.0.0.0:3005", "app:app"]
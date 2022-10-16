FROM python:3.10

RUN addgroup --gid 1000 server && adduser --uid 1000 --gid 1000 --system server
WORKDIR /home/server


RUN pip3 install gunicorn colorama upload flask pillow

USER server

COPY . .

ENV FLASK_APP app.py

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "app:app"]

FROM python:3.6

RUN apt-get update && apt-get upgrade -y

ADD /server /todo

WORKDIR /todo

RUN pip3 install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]



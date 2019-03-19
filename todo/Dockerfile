FROM python:3.6
RUN apt-get update && apt-get upgrade -y 
RUN pip3 install virtualenv\
    net-tools \
    django

RUN /bin -c 'source /bin/activate'
   
ADD /server /todo

CMD [ "python", "/todo/manage.py", "runserver", "0.0.0.0:8000" ]




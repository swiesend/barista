FROM python:3.5
MAINTAINER Sebastian Wiesendahl "sebastian@wiesendahl.de"
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["barista/app.py"]

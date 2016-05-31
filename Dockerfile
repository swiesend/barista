FROM python:3.5
MAINTAINER Sebastian Wiesendahl "sebastian@wiesendahl.de"
ADD . /tmp
WORKDIR /tmp
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["barista/app.py"]

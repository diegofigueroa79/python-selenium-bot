FROM python:3.6

RUN mkdir /code

WORKDIR code/

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD selenium_bot.py /code/

CMD ["python", "selenium_bot.py"]



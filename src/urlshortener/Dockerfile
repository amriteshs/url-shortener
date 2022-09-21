FROM python:3.9

RUN mkdir /url-shortener
WORKDIR /url-shortener
RUN pip install --upgrade pip gunicorn
COPY requirements.txt /url-shortener/

RUN pip install -r requirements.txt
COPY . /url-shortener/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
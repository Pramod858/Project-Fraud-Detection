FROM python:3.9.18-bullseye

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]
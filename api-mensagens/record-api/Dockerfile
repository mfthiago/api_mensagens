FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask mysql-connector-python redis

EXPOSE 5001

CMD ["python", "index.py"]

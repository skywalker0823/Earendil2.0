FROM --platform=linux/amd64 python:3.9

WORKDIR /code

COPY requirements.txt /code

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python3", "run.py"]
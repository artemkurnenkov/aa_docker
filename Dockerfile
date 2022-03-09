FROM python:3.9-slim-buster

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY /src /code/src

ENTRYPOINT [ "python", "/code/src/main.py" ]
EXPOSE 5001
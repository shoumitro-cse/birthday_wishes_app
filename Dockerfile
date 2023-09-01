FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /requirements.txt
RUN mkdir /src
WORKDIR /src
COPY . /src

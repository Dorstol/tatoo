FROM python:3.10

RUN apt update
RUN mkdir /tatoo

WORKDIR /tatoo

RUN mkdir /commands


COPY ./commands ./commands

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip \
    pip install -r ./requirements.txt

CMD ["bash"]
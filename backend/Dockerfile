FROM python:latest

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ${WORKDIR}

RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --disable-pip-version-check -r requirements.txt \
    && apt-get remove -y python3-pip \
    && apt-get autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

RUN adduser --disabled-password user

USER user

COPY . ${WORKDIR}

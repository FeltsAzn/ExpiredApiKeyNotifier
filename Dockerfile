FROM python:3.11.7
LABEL authors="tim"

WORKDIR /notifier
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y cron

ADD cron/cron_job /etc/cron.d/cron_job
RUN chmod 0644 /etc/cron.d/cron_job
RUN crontab /etc/cron.d/cron_job

COPY app/ .
COPY .env .env

CMD ["cron", "-f"]
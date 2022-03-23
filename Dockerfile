FROM python:3-alpine
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install gcc
COPY . ./
COPY --from=docker/compose:1.25.0-alpine /usr/local/bin/docker-compose /usr/local/bin/
EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]

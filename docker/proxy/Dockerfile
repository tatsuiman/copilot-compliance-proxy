FROM python:3.10

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./app /app
COPY ./settings.yaml /settings.yaml
COPY ./*.sh /
RUN cd /app/tests && pytest -v
WORKDIR /app
ENTRYPOINT ["/entrypoint.sh"]

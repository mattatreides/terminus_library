FROM python:3.9-alpine3.14

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY /scripts /scripts
RUN chmod +x -R /scripts/
RUN ls -alh /scripts
CMD ["/scripts/start.sh"]
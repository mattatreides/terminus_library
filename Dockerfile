FROM python:3.9-alpine3.14

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./scripts/start.sh /start.sh
RUN chmod +x /start.sh
COPY ./scripts/init_demo_data.sh /init_demo_data.sh
RUN chmod +x /init_demo_data.sh
ENV PYTHONPATH=/code
CMD ["/start.sh"]
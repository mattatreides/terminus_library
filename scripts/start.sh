#! /usr/bin/env sh
# Create initial data in DB
python /code/app/init_data.py
exec uvicorn app.main:app --host 0.0.0.0 --port 80

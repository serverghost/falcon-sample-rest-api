FROM python:3.8-slim
WORKDIR /app
ADD app/requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt
ADD app/ /app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0", "app:api"]
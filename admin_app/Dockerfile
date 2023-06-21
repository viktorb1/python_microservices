FROM python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD python manage.py wait_for_db && \
    python manage.py migrate && \
    python manage.py populate_ambassadors && \
    python manage.py populate_orders && \
    python manage.py populate_products && \
    python manage.py update_rankings && \
    python manage.py runserver 0.0.0.0:8000
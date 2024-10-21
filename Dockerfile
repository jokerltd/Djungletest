FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -m jester
USER jester

ENV PATH="/home/jester/.local/bin:${PATH}"

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip --no-warn-script-location && \
    pip install --no-cache-dir -r requirements.txt
RUN pip install djangorestframework-simplejwt

COPY --chown=jester:jester . /app/

EXPOSE 8000

CMD ["gunicorn", "DjungleTest.wsgi:application", "--bind", "0.0.0.0:8100"]





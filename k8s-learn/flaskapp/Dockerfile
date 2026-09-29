FROM python:3.13-alpine3.23 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/usr/local -r requirements.txt

FROM python:3.13-alpine3.23
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app.py .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

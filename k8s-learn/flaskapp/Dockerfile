FROM python:3.13-alpine3.23 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.13-alpine3.23
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
RUN adduser -D appuser
RUN chown appuser /app
RUN chmod 0755 /app
USER appuser
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

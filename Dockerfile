FROM python:3.12-slim
WORKDIR /app
COPY index.html .
RUN pip install --no-cache-dir flask gunicorn
COPY server.py .
ENV PORT=8080
CMD gunicorn --bind 0.0.0.0:$PORT server:app

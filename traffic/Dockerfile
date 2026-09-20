FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pymodbus==2.5.3

COPY traffic.py /app/traffic.py

CMD ["python", "-u", "/app/traffic.py"]
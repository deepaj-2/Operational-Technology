FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pymodbus==2.5.3

COPY attacker.py /app/attacker.py

CMD ["python", "-u", "/app/attacker.py"]
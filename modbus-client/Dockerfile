FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pymodbus==2.5.3

COPY read_write.py /app/read_write.py

CMD ["python", "/app/read_write.py"]
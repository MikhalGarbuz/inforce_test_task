FROM python:3.13-slim

WORKDIR /src

COPY requirements.txt .

RUN apt update \
    && apt install -y libpq-dev gcc \ 
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/etl.py"]
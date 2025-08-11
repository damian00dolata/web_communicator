FROM python:3.9.17-bookworm

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      sqlite3 libsqlite3-dev \
      build-essential python3-dev libffi-dev libssl-dev \
      cargo \
 && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir 'uvicorn[standard]' bcrypt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:mainApp.restApi.app", "--host","0.0.0.0","--port","8000"]

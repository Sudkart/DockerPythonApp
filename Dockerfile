# FROM python:3.8

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .

# CMD ["python", "app.py"]

# Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]

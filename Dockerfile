# Do not change the base image
FROM python:3.8
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY program.py .

CMD ["python", "program.py"]
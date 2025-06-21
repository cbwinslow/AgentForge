FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r REQUIREMENTS.txt
CMD ["python", "webapp/app.py"]

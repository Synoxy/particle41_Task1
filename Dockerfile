FROM python:3.10-slim
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
RUN useradd --create-home --shell /bin/bash appuser
USER appuser
CMD ["python", "app.py"]
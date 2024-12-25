FROM python:3.9-slim

# Установите зависимости
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте код приложения
COPY . /app

# Настройте команду запуска
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
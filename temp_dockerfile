# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY . /app/

# Собираем статические файлы
RUN python manage.py collectstatic --noinput


# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["gunicorn", "FlyFishingSport.wsgi:application", "--bind", "0.0.0.0:8000"]

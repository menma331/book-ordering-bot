# Используем базовый образ Python версии 3.11
FROM python:3.11

# Устанавливаем переменную окружения для указания на использование Python в режиме не-буферизованного вывода
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости приложения (файл requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости приложения
RUN python -m pip install --no-cache-dir --quiet -r requirements.txt


# Копируем все файлы нашего приложения в контейнер
COPY main.py .
COPY Connection.py .
COPY handlers.py .
COPY keyboard.py .
COPY State.py .

# Укажите порт для приложения
# EXPOSE 5000

# Запускаем наше приложение при старте контейнера
CMD ["python", "main.py"]

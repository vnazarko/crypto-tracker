# Базовый образ Python
FROM python:3.12.3

# Создаем директорию для приложения
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости Python и chromedriver-autoinstaller
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install chromedriver-autoinstaller

# Устанавливаем Google Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    unzip \
    libgconf-2-4 \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем все файлы приложения в контейнер
COPY . .

# Определяем команду для запуска приложения
CMD ["python3", "src/main.py"]

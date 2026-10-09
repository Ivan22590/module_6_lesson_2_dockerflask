# Flask + Docker test app

Простое Flask-приложение для тестирования контейнера в Docker.

## Локальный запуск

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Приложение доступно на http://localhost:5000

## Сборка образа

```powershell
docker build -t flask-test .
```

## Запуск контейнера

```powershell
docker run -p 5000:5000 flask-test
```

## Docker Compose (backend + frontend)

В `docker-compose.yml` объединены два сервиса:

- **backend** — Flask-приложение, образ из Docker Hub (`ivan22590/flask-backend:latest`), порт наружу не публикуется
- **frontend** — nginx: отдаёт веб-интерфейс и проксирует `/api/*` на `backend:5000` по внутренней сети compose

Схема запроса: `браузер → localhost:8080 (frontend/nginx) → backend:5000 (внутри compose)`

```powershell
docker compose up --build
```

- Веб-интерфейс: http://localhost:8080 — статус бэкенда (автообновление) и калькулятор умножения
- Остановка: `docker compose down`

## Проверка

- Откройте http://localhost:5000 — приветственная страница с hostname и версией Python
- Откройте http://localhost:5000/health — JSON `{"status": "ok", ...}`

Или через PowerShell:

```powershell
Invoke-WebRequest http://localhost:5000/health
```

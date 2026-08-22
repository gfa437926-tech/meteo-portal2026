@echo off
REM =========================================================
REM Sovereign Meteorological Portal - 1-Click Docker Launch
REM Country: الجمهورية العربية السورية
REM Agency:  General Directorate of Meteorology - Syria
REM =========================================================

echo =========================================================
echo 🌪️  Starting Sovereign Meteorological Portal in Docker...
echo =========================================================

docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Docker is not installed or Docker Desktop is not running.
    echo 👉 Please install or start Docker Desktop: https://www.docker.com/
    pause
    exit /b 1
)

echo ⚙️  Building and starting containers...
docker compose up -d --build

echo.
echo =========================================================
echo ✅ Sovereign Meteorological Portal is now LIVE!
echo 🌐 Public Citizen Portal: http://localhost:8080
echo 🔒 Standalone CMS Admin:  http://localhost:8080/admin
echo 📖 Docker & Cloud Guide:  http://localhost:8080/guide.html
echo 📡 Health API Endpoint:   http://localhost:8080/api/agency
echo =========================================================
echo Opening browser...
start http://localhost:8080
pause

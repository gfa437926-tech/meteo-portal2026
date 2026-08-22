#!/bin/bash
# =========================================================
# Sovereign Meteorological Portal - 1-Click Docker Launch
# Country: الجمهورية العربية السورية
# Agency:  General Directorate of Meteorology - Syria
# Backend: PYTHON
# =========================================================

echo "========================================================="
echo "🌪️  Starting Sovereign Meteorological Portal in Docker..."
echo "========================================================="

if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed or Docker engine is not running."
    echo "👉 Please install Docker Desktop from https://www.docker.com/"
    exit 1
fi

docker compose up -d --build

echo ""
echo "========================================================="
echo "✅ Sovereign Meteorological Portal is now LIVE!"
echo "🌐 Public Citizen Portal: http://localhost:8080"
echo "🔒 Standalone CMS Admin:  http://localhost:8080/admin"
echo "📖 Docker & Cloud Guide:  http://localhost:8080/guide.html"
echo "📡 Health API Endpoint:   http://localhost:8080/api/agency"
echo "========================================================="

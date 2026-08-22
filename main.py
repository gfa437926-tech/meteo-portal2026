"""
Sovereign Meteorological Portal & REST Service (Python FastAPI)
Agency: General Directorate of Meteorology - Syria
Country: الجمهورية العربية السورية
"""
import json
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="General Directorate of Meteorology - Syria Sovereign API",
    description="WMO Standard CAP 1.2 and Weather Portal Service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "database.json")

def load_db():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading database: {e}")
        return None

# API: Agency Profile & Dual Logos
@app.get("/api/agency")
def get_agency():
    db = load_db()
    if not db:
        return {
            "status": "online",
            "country": "الجمهورية العربية السورية",
            "agency": "General Directorate of Meteorology - Syria",
            "wmo_id": "WMO-40080",
            "timestamp": datetime.utcnow().isoformat()
        }
    return {
        "agency": db.get("agency"),
        "branding": db.get("branding"),
        "country": "الجمهورية العربية السورية",
        "emblem": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=160&auto=format&fit=crop&q=80",
        "logo": "https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=160&auto=format&fit=crop&q=80",
        "primaryLanguage": "ar",
        "direction": "rtl"
    }

# API: Cities Forecasts
@app.get("/api/cities")
def get_cities():
    db = load_db()
    if not db:
        raise HTTPException(status_code=500, detail="Database unavailable")
    return db.get("cities", [])

# API: CAP Alerts JSON
@app.get("/api/alerts")
def get_alerts():
    db = load_db()
    if not db:
        raise HTTPException(status_code=500, detail="Database unavailable")
    return {
        "agency": "General Directorate of Meteorology - Syria",
        "wmoStation": "WMO-40080",
        "timestamp": datetime.utcnow().isoformat(),
        "alerts": db.get("alerts", [])
    }

# API: WMO Standard CAP 1.2 XML Feed
@app.get("/api/cap/feed.xml")
def get_cap_xml():
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:cap="urn:oasis:names:tc:emergency:cap:1.2">
  <title>General Directorate of Meteorology - Syria CAP Warnings Feed</title>
  <id>WMO-40080</id>
  <updated>{datetime.utcnow().isoformat()}</updated>
</feed>"""
    return Response(content=xml_content, media_type="application/xml")

# Mount static public files (Citizen Portal & Admin CMS)
if os.path.exists(os.path.join(os.path.dirname(__file__), "public")):
    app.mount("/", StaticFiles(directory="public", html=True), name="public")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    print("=" * 50)
    print("🌪️  General Directorate of Meteorology - Syria (Python FastAPI)")
    print(f"📍  Running on port {port}")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=port)

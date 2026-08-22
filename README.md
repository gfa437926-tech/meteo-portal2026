# المديرية العامة للأرصاد الجوية السورية
## General Directorate of Meteorology - Syria — Sovereign Meteorological Portal, CMS & Cloud Bundle

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

* **Country:** الجمهورية العربية السورية 🇸🇾
* **Backend Stack:** PYTHON
* **Mobile App:** Flutter (Dart) Cross-Platform Included ✅
* **WMO Station ID:** WMO-40080

---

## 🐳 دليل تشغيل دوكر السريع ومحلياً (Docker & Local Run Guide)

### 1. التشغيل المحلي بضغطة زر واحدة (1-Click Run):
* **على نظام Windows:** انقر نقراً مزدوجاً على ملف `start.bat`.
* **على أنظمة Linux / macOS:** نفّذ الأمر `chmod +x start.sh && ./start.sh` أو الأمر:
```bash
docker compose up -d --build
```

بمجرد تشغيل الحاوية، ستكون جميع المكونات متاحة على الروابط التالية:
* **البوابة العامة للمواطنين:** [http://localhost:8080](http://localhost:8080)
* **لوحة تحكم المشرف (CMS):** [http://localhost:8080/admin](http://localhost:8080/admin)
* **صفحة دليل التشغيل التفاعلية:** [http://localhost:8080/guide.html](http://localhost:8080/guide.html)
* **واجهة برمجة التطبيقات (API):** [http://localhost:8080/api/agency](http://localhost:8080/api/agency)

---

### 2. النشر السحابي بضغطة زر (One-Click Cloud Launch):
1. **Render.com**: ارفع هذا المستودع إلى GitHub ثم اختر New Blueprint.
2. **Railway.app**: اختر New Project -> Deploy from GitHub.
3. **Fly.io**: نفّذ `fly launch` في المجلد الرئيسي.

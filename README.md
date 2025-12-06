# 🌦 Időjárás Mikroszerviz – FastAPI + Streamlit

Ez a projekt a **Multi Paradigmás Programozási Nyelvek** tantárgy beadandó feladatához készült.  
A rendszer egy egyszerű, mégis mikroszerviz-szerű Python alapú alkalmazás, amely külön **backend**, **frontend**, **adatbázis** és **automatizációs** rétegekre épül.

---

## 📋 Tartalomjegyzék

- [Főbb Funkciók](#-főbb-funkciók)
- [Projekt Architektúra](#-projekt-architektúra)
- [Telepítés és Indítás](#-telepítés-és-indítás)
- [Használat](#-használat)
- [API Végpontok](#-api-végpontok)
- [Projekt Struktúra](#-projekt-struktúra)
- [Technológiák](#-technológiák)
- [Tesztelés](#-tesztelés)
- [Környezeti Változók](#-környezeti-változók)
- [Fejlesztés](#-fejlesztés)

---

## ✨ Főbb Funkciók

- 🌍 **Időjárási adatok lekérése** az OpenWeather API-ból
- 💾 **Adatok mentése** SQLite adatbázisba SQLAlchemy ORM használatával
- 🔌 **REST API végpontok** FastAPI keretrendszerrel
- 📊 **Modern, interaktív frontend** Streamlit segítségével
- ⏰ **Automatikus háttérfolyamat**, amely óránként frissíti az időjárási adatokat
- ✅ **Pytest egységtesztek**, köztük paraméterezett tesztek
- ⚙️ **Környezeti változók kezelése** `.env` fájllal
- 📈 **Statisztikák és grafikonok** a hőmérsékleti trendekről

A rendszer demonstrálja a **procedurális**, **funkcionális** és **objektumorientált** programozási paradigmák használatát.

---

## 🏗 Projekt Architektúra

```
┌─────────────────┐
│  Streamlit UI   │  ← Frontend (port 8501)
└────────┬────────┘
         │ HTTP
         ↓
┌─────────────────┐
│   FastAPI       │  ← Backend REST API (port 8000)
└────────┬────────┘
         │
    ├────┴────┬──────────┐
    ↓         ↓          ↓
┌────────┐ ┌──────┐ ┌──────────┐
│SQLite  │ │OpenW.│ │Scheduler │
│  DB    │ │ API  │ │(óránként)│
└────────┘ └──────┘ └──────────┘
```

### Rétegek

1. **Frontend (Streamlit)**: Felhasználói felület, grafikonok és táblázatok megjelenítése
2. **Backend (FastAPI)**: REST API szolgáltatás, üzleti logika
3. **Adatbázis (SQLite)**: Időjárási adatok perzisztens tárolása
4. **Külső API (OpenWeather)**: Valós idejű időjárási adatok forrása
5. **Scheduler**: Automatikus időzített adatfrissítés

---

## 🚀 Telepítés és Indítás

### Előfeltételek

- **Python 3.8+** telepítve
- **pip** csomagkezelő
- **OpenWeather API kulcs** (ingyenes regisztráció: https://openweathermap.org/)

### 1. Projekt klónozása

```bash
git clone <repository-url>
cd Multi_beadando
```

### 2. Virtuális környezet létrehozása (opcionális, de ajánlott)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Függőségek telepítése

```bash
pip install -r requirements.txt
```

### 4. Környezeti változók beállítása

Hozz létre egy `.env` fájlt a projekt gyökérkönyvtárában:

```env
OPENWEATHER_API_KEY=your_api_key_here
DB_URL=sqlite:///./weather.db
CITY=Budapest
```

### 5. Alkalmazás indítása

#### Opció A: Mindkét szolgáltatás automatikus indítása (Linux/Mac)

```bash
bash start.sh
```

#### Opció B: Manuális indítás (Windows/Linux/Mac)

**Terminál 1 - Backend indítása:**
```bash
uvicorn backend.main:app --reload
```

**Terminál 2 - Frontend indítása:**
```bash
streamlit run frontend/app.py
```

### 6. Alkalmazás megnyitása

- **Frontend (Streamlit)**: http://localhost:8501
- **Backend API (FastAPI)**: http://localhost:8000
- **API Dokumentáció**: http://localhost:8000/docs

---

## 📊 Használat

### Frontend Dashboard

A Streamlit alapú felhasználói felület a következő funkciókat kínálja:

1. **Statisztikai Áttekintés**
   - Átlaghőmérséklet
   - Maximum hőmérséklet (delta mutatóval)
   - Minimum hőmérséklet (delta mutatóval)
   - Mérések száma

2. **Aktuális Időjárás**
   - Jelenlegi hőmérséklet nagy, kiemelten
   - Időjárás leírása ikonsokkal
   - Város és időbélyeg

3. **Hőmérsékleti Trend**
   - Vonaldiagram a hőmérsékleti változásokról
   - Részletes adatok táblázatban (expandálható)

4. **Automatikus frissülés**
   - A backend óránként frissíti az adatokat
   - A Streamlit oldalon frissítés szükséges az új adatok láthatóságához

---

## 🔌 API Végpontok

### Base URL: `http://localhost:8000`

#### 1. **GET /weather/latest**
Visszaadja a legfrissebb időjárási adatot.

**Válasz példa:**
```json
{
  "id": 15,
  "city": "Budapest",
  "temperature": 8.5,
  "description": "clear sky",
  "timestamp": "2025-12-06 22:00:00"
}
```

#### 2. **GET /weather/history**
Visszaadja az összes elmentett időjárási adatot.

**Válasz példa:**
```json
[
  {
    "id": 1,
    "city": "Budapest",
    "temperature": 7.2,
    "description": "cloudy",
    "timestamp": "2025-12-06 10:00:00"
  },
  ...
]
```

#### 3. **GET /weather/stats**
Hőmérsékleti statisztikák (minimum, maximum, átlag).

**Válasz példa:**
```json
{
  "min": 5.2,
  "max": 12.8,
  "avg": 8.7
}
```

#### 4. **GET /weather/refresh**
Manuálisan frissíti az időjárási adatokat (új lekérés az OpenWeather API-ból).

**Válasz példa:**
```json
{
  "city": "Budapest",
  "temperature": 9.1,
  "description": "light rain",
  "timestamp": "2025-12-06 22:30:00"
}
```

### Interaktív API Dokumentáció

FastAPI automatikusan generál Swagger UI dokumentációt:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📁 Projekt Struktúra

```
Multi_beadando/
│
├── backend/                    # Backend alkalmazás
│   ├── __init__.py
│   ├── main.py                 # FastAPI alkalmazás belépési pontja
│   ├── config.py               # Környezeti változók kezelése
│   ├── database.py             # SQLAlchemy adatbázis beállítások
│   │
│   ├── api/                    # API végpontok
│   │   ├── __init__.py
│   │   └── weather_api.py      # Időjárás API router
│   │
│   ├── models/                 # ORM modellek
│   │   ├── __init__.py
│   │   └── weather_model.py    # Weather adatbázis modell
│   │
│   └── services/               # Üzleti logika
│       ├── __init__.py
│       ├── weather_service.py  # OpenWeather API integráció
│       └── scheduler.py        # Időzített feladatok
│
├── frontend/                   # Frontend alkalmazás
│   └── app.py                  # Streamlit dashboard
│
├── tests/                      # Tesztek
│   ├── test_api.py             # API tesztek
│   ├── test_model.py           # Modell tesztek
│   └── test_stats_parametrize.py  # Paraméterezett tesztek
│
├── .env                        # Környezeti változók (NEM commitolva)
├── requirements.txt            # Python függőségek
├── start.sh                    # Indító script (Linux/Mac)
├── weather.db                  # SQLite adatbázis (automatikusan létrejön)
└── README.md                   # Projekt dokumentáció
```

---

## 🛠 Technológiák

### Backend
- **FastAPI**: Modern, gyors Python web framework
- **SQLAlchemy**: SQL toolkit és ORM
- **Uvicorn**: ASGI szerver
- **Pydantic**: Adatvalidáció
- **python-dotenv**: Környezeti változók kezelése
- **schedule**: Időzített feladatok

### Frontend
- **Streamlit**: Interaktív web alkalmazások Pythonban
- **Pandas**: Adatelemzés
- **Requests**: HTTP könyvtár

### Tesztelés
- **Pytest**: Python tesztelési framework

### Adatbázis
- **SQLite**: Lightweight SQL adatbázis

### Külső API
- **OpenWeather API**: Időjárási adatok szolgáltatója

---

## ✅ Tesztelés

### Tesztek futtatása

```bash
pytest
```

### Verbose mód (részletes kimenet)

```bash
pytest -v
```

### Specifikus teszt fájl futtatása

```bash
pytest tests/test_api.py
```

### Tesztek leírása

1. **test_api.py**: API végpontok tesztelése
2. **test_model.py**: Weather modell tesztelése
3. **test_stats_parametrize.py**: Statisztikai számítások paraméterezett tesztje

---

## ⚙️ Környezeti Változók

A `.env` fájl a következő változókat tartalmazza:

| Változó | Leírás | Alapértelmezett | Kötelező |
|---------|--------|-----------------|----------|
| `OPENWEATHER_API_KEY` | OpenWeather API kulcs | - | ✅ Igen |
| `DB_URL` | SQLite adatbázis URL | `sqlite:///./weather.db` | ❌ Nem |
| `CITY` | Város, amelynek időjárását lekérjük | `Budapest` | ❌ Nem |

### OpenWeather API kulcs megszerzése

1. Regisztrálj: https://openweathermap.org/
2. Lépj be és generálj ingyenes API kulcsot
3. Másold be a `.env` fájlba

---

## 💻 Fejlesztés

### Új API végpont hozzáadása

1. Hozz létre új endpoint függvényt a `backend/api/weather_api.py`-ban
2. Használj router decoratort: `@router.get("/my-endpoint")`
3. A végpont automatikusan elérhető lesz a `/weather/my-endpoint` címen

### Új adatmező hozzáadása

1. Bővítsd a `Weather` modellt (`backend/models/weather_model.py`)
2. Töröld a `weather.db` fájlt vagy használj migrációt
3. Indítsd újra az alkalmazást - az adatbázis automatikusan létrejön

### Időzítés módosítása

A `backend/services/scheduler.py` fájlban található a háttérfolyamat:

```python
# Példa: 30 percenkénti frissítés
schedule.every(30).minutes.do(fetch_weather)
```

### Frontend testreszabása

A `frontend/app.py` fájlt módosítva alakíthatod a megjelenést:
- Custom CSS a `st.markdown()` blokkon belül
- Új szekciók hozzáadása
- Grafikonok típusának módosítása

---

## 📝 Megjegyzések

- Az alkalmazás indításakor automatikusan létrejön a `weather.db` SQLite adatbázis
- A scheduler automatikusan elindul a backend indulásakor
- Az első adatok az első indítás után azonnal megjelennek
- A frontend az API-ból tölti be az adatokat minden frissítéskor

---

## 🎓 Készítette

**Multi Paradigmás Programozási Nyelvek - Beadandó Feladat**  
EKKE - Eger

---

## 📄 Licenc

Ez a projekt oktatási célokra készült.

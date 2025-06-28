Weather forecast API
========================
This is a simple weather forecast API that provides weather forecast data for a given city.

API Endpoints
========================

| Method | URL                      | Description                              |
| ------ | ------------------------ | ---------------------------------------- |
| POST   | `/api/register/`         | Register a new user                      |
| POST   | `/api/token/`            | Login and receive auth token             |
| POST   | `/api/forecast/`         | Request forecast by location, date, time |
| GET    | `/api/forecast/history/` | List past forecasts (premium only)       |
| POST   | `/api/payment/`          | Fake payment to become premium           |

Admin Panel
========================
Access via: /admin/

- Insert forecasts manually under ForecastData
- Add users and promote them as premium manually if needed

Notes
========================

- Forecasts are stored in ForecastData, and matched exactly by location, date, time
- Only forecasts with time in full hours (e.g., 14) are supported
- Time dropdown in DRF API shows only full hours (00–23)
- All requests and limits are applied based on user OR anonymous session ID
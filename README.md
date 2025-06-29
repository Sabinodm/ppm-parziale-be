Weather forecast API
========================
This is a simple weather forecast API that provides weather forecast data for a given city.

Database population
========================
The database is populated with sample data using the `pop_database.py` script. This script creates a set of forecasts for Firenze, from 06/28/2025 to 07/13/2025, with hourly forecasts at full hours (00–23).

User types and access levels
========================
| User Type  | Access Level | Requests per day | Forecasts History |
|------------|--------------|------------------|-------------------|
| Anonymous  | Free         | 10               | No                |
| Registered | Free         | 10               | No                |
| Premium    | Paid         | Unlimited        | Yes               |

Usage for premium users
========================
1. **Register a new user**: Use the `/user/register/` endpoint to create a new user account.
2. **Login**: Use the `/auth/login/` endpoint to log in and receive an authentication token.
3. **Become a premium user**: Use the `/user/payment/` endpoint to simulate a payment and gain premium access.
4. **Request a forecast**: Use the `/api/forecast/` endpoint to get the weather forecast for a specific location, date, and time.
5. **View past forecasts**: Premium users can access the `/api/forecast/history/` endpoint to view their past forecasts.

API Endpoints
========================

| Method | URL                      | Description                              |
|--------|--------------------------|------------------------------------------|
| POST   | `/user/register/`        | Register a new user                      |
| POST   | `/user/payment/`         | Simulate payment to become premium       |
| POST   | `/auth/login/`           | Login and receive auth token             |
| POST   | `/api/forecast/`         | Request forecast by location, date, time |
| GET    | `/api/forecast/history/` | List past forecasts (premium only)       |


Preregistered users
========================
| Username | Password      | Premium |
|----------|---------------|---------|
| JohnDoe  | Random.123456 | Yes     |

Admin Panel
========================
Access via: `/admin/`

Staff credentials:

| Username | Password      |
|----------|---------------|
| Staff    | Staff         |

- Insert forecasts manually under ForecastData
- Add users and promote them as premium manually if needed

Notes
========================

- Forecasts are stored in ForecastData, and matched exactly by location, date, time
- Only forecasts with time in full hours (e.g., 14) are supported
- Time dropdown in DRF API shows only full hours (00–23)
- All requests and limits are applied based on user OR anonymous session ID
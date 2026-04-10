# Extreme Climate Events Analysis in United States

Predictive analysis of extreme weather events trends in the US using NOAA data and machine learning.

This analysis covers records from NOAA (National Oceanic and Atmospheric Administration) for the years 2000–2024.

---

## Tech Stack

- **SQL (SQLite)** — data extraction and aggregation
- **Pandas** — data cleaning and feature engineering
- **Matplotlib / Seaborn** — exploratory visualizations
- **Scikit-learn / XGBoost** — predictive modeling
- **Plotly** — interactive dashboard

---

## Data Pipeline

```
Raw CSV (NOAA)  →  SQLite database  →  SQL queries  →  Pandas  →  Model  →  Dashboard
```

---

## Project Phases

**1. Exploratory Data Analysis** (Finished)
- Frequency trends by event type
- Geographic analysis (most affected states)
- Temporal analysis (decades, years, months)
- Correlation between event types

**2. Feature Engineering**
- Annual frequency by state
- Moving average of events
- Seasonality index
- Severity index (based on damages and deaths)

**3. Predictive Modeling**
- Linear Regression (baseline) — predict event frequency for next year
- Random Forest / XGBoost — predict probability of extreme events by region
- Evaluation: RMSE, MAE, R²

**4. Dashboard**
- Interactive event map
- Trend charts
- Forecasts for the next 5 years

---

## Notebooks

| Notebook | Description |
|---|---|
| [00 — Database Setup](notebooks/00_database_setup.py) | Loads CSVs into SQLite database |
| [01 — Data Exploration](https://github.com/Lucasqrz1/us_extreme_weather_prediction/blob/main/notebooks/01_data_exploration.ipynb) | EDA, trends, geographic and temporal analysis |
| [02 — Feature Engineering](notebooks/02_feature_engineering.ipynb) | Feature creation and transformation |

---

## Sample Insights

![Extreme Weather Events Over Time](/images/01_events_trend.png)

---

![Top 10 Most Frequent Event Types](/images/02_top_event_types.png)
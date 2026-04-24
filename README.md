# Extreme Climate Events Analysis in United States (Mainland)

Predictive analysis of extreme weather events trends in the US (Mainland states only) using NOAA data and machine learning.

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

**1. Exploratory Data Analysis** ✅
- Frequency trends by event type
- Geographic analysis (most affected states)
- Temporal analysis (decades, years, months)
- Correlation between event types

**2. Feature Engineering** ✅
- Annual event frequency per state
- 3-year rolling average of events
- Seasonality (month, quarter, peak season flag)
- Severity index — normalized combination of economic damage and fatalities

**3. Predictive Modeling** ✅
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
| [00 — Database Setup](notebooks/00_database_setup.ipynb) | Loads CSVs into SQLite database |
| [01 — Data Exploration](notebooks/01_data_exploration.ipynb) | EDA, trends, geographic and temporal analysis |
| [02 — Feature Engineering](notebooks/02_feature_engineering.ipynb) | Feature creation and transformation |
| [03 — Predictive Modeling](notebooks/03_predictive_modeling.ipynb) | Linear Regression, Random Forest, and XGBoost model training and evaluation |

---

## Sample Insights

![Extreme Weather Events Over Time](/images/01_events_trend.png)

---

![Top 10 Most Frequent Event Types](/images/02_top_event_types.png)

## Next Steps

- Evaluate possibility of only analising mainland states
- Understand noise caused by innacurate information on charts (e.g. American Samoa)
- Review datasets that are being used throughout different notebooks and if they're being affected by innacurate info
- Create interactive dashboards with Plotly
- Evaluate possibility of using AI to support project development (e.g. Ollama)
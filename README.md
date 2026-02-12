# Extreme Climate Events Analysis in United States

### Predictive analysis of extreme weather events trends in the US using NOAA data and machine learning.

This analysis covers records of the United States NOAA (National Oceanic and Atmospheric Administration) using, from a broader database, a selection of the years 2000 up to 2024.


The project consists in 4 phases: 

1. Exploratory Data Analysis

    - Frequency trends by event type
    - Geographic analysis (most affected states)
    - Temporal analysis (decades, years, months)
    - Correlation between event types
    - Tools: SQL + Python (Pandas, Matplotlib, Seaborn)
    
2. Feature Engineering

    - Create derived variables:
        - Annual frequency by state
        - Moving average of events
        - Seasonality
        - Severity index (based on damages/deaths)
    - Tools: Python (Pandas, NumPy)

3. Predictive Modeling

    - Model 1: Linear Regression (simple baseline)
    - Predict event frequency for the next year
    - Model 2: Random Forest or XGBoost (more robust)
    - Predict probability of extreme events by region
    - Evaluation: RMSE, MAE, R²
    - Tools: Python (Scikit-learn, XGBoost)

4. Dashboard / Visualizations

    - Interactive event map
    - Trend charts
    - Forecasts for the next 5 years
    - Tools: Python (Plotly) or Tableau / Power BI

## Notebooks

- [Data Exploration](https://github.com/Lucasqrz1/us_extreme_weather_prediction/blob/main/notebooks/01_data_exploration.ipynb)

## Images

![Top 10 Most Frequent Event Types](/images/01_events_trend.png)
---
![Extreme Weather Events in the US Over Time](/images/02_top_event_types.png)

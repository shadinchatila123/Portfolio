# Transportation Analysis: Impact of Extreme Weather on Monthly Usage

## **Overview**
This project explores the relationship between extreme weather events and monthly transportation usage patterns. By integrating weather data with transportation statistics, the analysis aims to identify correlations and trends that can inform decision-making in urban planning and transportation management.

## **Objectives**
- Analyze the impact of extreme weather events on transportation usage.
- Identify patterns and trends in monthly usage affected by weather conditions.
- Provide recommendations for mitigating disruptions caused by adverse weather.

## **Technologies Used**
- **Python**: Data integration and analysis.
- **Pandas**: Data cleaning, transformation, and aggregation.
- **Matplotlib & Seaborn**: Visualizations (line charts, scatter plots, etc.).
- **OpenWeatherMap API**: Weather data collection.
- **Jupyter Notebook**: Interactive data analysis.

## **Key Analysis Steps**
1. **Data Integration**:
   - Combined transportation statistics from Kaggle with weather data from the OpenWeatherMap API.
   - Aligned datasets temporally to ensure consistency in monthly analysis.

2. **Exploratory Data Analysis (EDA)**:
   - Visualized monthly transportation usage trends over time.
   - Analyzed correlations between extreme weather events (e.g., heavy rainfall, snowstorms) and dips or surges in transportation usage.

3. **Visualizations**:
   - Line graphs showing transportation usage over time.
   - Scatter plots correlating weather severity indices with usage changes.

4. **Insights**:
   - Identified significant dips in transportation usage during severe weather events.
   - Highlighted periods of recovery after extreme conditions, varying by region.

## **Results**
- Usage of public transportation drops significantly during severe weather conditions such as snowstorms and heavy rainfall.
- Recovery patterns depend on the severity and duration of the weather event as well as regional preparedness.

## **Recommendations**
1. Invest in weather-resilient infrastructure for public transportation systems.
2. Develop contingency plans to ensure service availability during adverse weather conditions.
3. Communicate potential disruptions effectively to commuters based on predictive weather analytics.

## **How to Run**
1. **Data Preparation**:
   - Ensure transportation and weather datasets are available and properly formatted.
   - Obtain an API key from OpenWeatherMap for live weather data collection.

2. **Execute the Analysis**:
   - Open the `Transportation_Analysis.ipynb` Jupyter Notebook.
   - Run all cells to process the data and generate visualizations.

## **Files Included**
- `Transportation_Analysis.ipynb`: Python code for data analysis and visualization.
- Weather data (not included; must be retrieved using OpenWeatherMap API).
- Transportation statistics from Kaggle (link or source details should be added).

## **Future Enhancements**
- Incorporate real-time data streams for live monitoring of transportation disruptions.
- Use machine learning models to predict transportation usage based on forecasted weather conditions.
- Analyze regional differences in weather impact to tailor recommendations.

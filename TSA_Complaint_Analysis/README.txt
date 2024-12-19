# TSA Complaint Analysis

## **Overview**
This project analyzes TSA complaint data to uncover patterns and identify key areas for improvement. The insights are intended to help TSA executives and decision-makers enhance passenger satisfaction and streamline operational processes.

## **Objectives**
- Identify high-complaint airports and their most common complaint categories.
- Analyze seasonal trends and subcategories of complaints.
- Provide actionable recommendations to reduce complaint volumes.

## **Technologies Used**
- **Python**: Data analysis and visualization.
- **Pandas**: Data cleaning and aggregation.
- **Seaborn & Matplotlib**: Visualizations (heatmaps, scatter plots, line charts, etc.).
- **Jupyter Notebook**: Interactive data analysis.
- **PowerPoint**: Presentation layer for executive reporting.

## **Key Visualizations**
1. **Line Chart**: Shows monthly trends in complaint volumes.
2. **Heat Map**: Displays monthly distribution of complaints by category.
3. **Box Plot**: Highlights variability in complaint counts by category.
4. **Scatter Plot**: Maps complaint volumes by airport location.
5. **Bubble Chart**: Illustrates top complaint categories at high-complaint airports.

## **Results**
- High complaint areas include:
  - Screening processes.
  - Mishandling of property.
  - Wait times.
- Seasonal spikes in complaints correlate with peak travel months.
- Specific airports, such as EWR, consistently show high complaint volumes.

## **Recommendations**
1. Enhance training in high-complaint areas such as property handling and screening procedures.
2. Allocate additional resources to high-complaint airports during peak travel seasons.
3. Implement targeted improvement initiatives for specific issues at major airports.

## **How to Run**
1. **Data Preparation:**
   - Ensure the required datasets are in the working directory:
     - `complaints-by-airport.csv`
     - `complaints-by-category.csv`
     - `complaints-by-subcategory.csv`
     - `iata-icao.csv`

2. **Execute the Analysis:**
   - Open the `TSA_Complaint_Python.ipynb` Jupyter Notebook.
   - Run all cells to generate visualizations and insights.

3. **Presentation:**
   - Review the PowerPoint file (`TSA_Complaint_Prezy.pdf`) for a concise summary of the analysis and recommendations.

## **Files Included**
- `TSA_Complaint_Python.ipynb`: Python code for data analysis and visualization.
- `TSA_Complaint_Analysis.pdf`: Detailed project write-up.
- `TSA_Complaint_Prezy.pdf`: Executive presentation with visual summaries.

## **Future Enhancements**
- Automate real-time data processing for continuous monitoring.
- Integrate machine learning to predict high-complaint periods and locations.

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Construct the URL with the current year
url = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={current_year}"

# Columns to extract
columns_to_extract = ["Date", "1 Mo", "2 Mo", "3 Mo", "6 Mo", "1 Yr", "2 Yr", "3 Yr", "5 Yr", "7 Yr", "10 Yr", "20 Yr",
                      "30 Yr"]

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table element with specific class name
    table = soup.find("table", class_="usa-table views-table views-view-table cols-23")

    # Check if the table exists
    if table:
        # Extract table headers
        headers = [header.text.strip() for header in table.find_all("th")]

        # Initialize a list to store rows of data
        data = []

        # Extract table rows and filter selected columns
        rows = table.find_all("tr")
        for row in rows:
            # Extract cells from the row
            cells = row.find_all("td")
            # Filter cells to include only data for specified columns
            selected_cells = [cell.text.strip() for header, cell in zip(headers, cells) if header in columns_to_extract]
            # Add selected cells to the data list
            if selected_cells:
                data.append(selected_cells)

        # Create a DataFrame using the extracted data and headers
        df = pd.DataFrame(data, columns=columns_to_extract)

        # Print the DataFrame (optional)
        print(df)

        # Now you can work with the DataFrame 'df' as desired

        print("Data has been scraped and stored in a DataFrame.")
    else:
        print("Table with specific class name not found on the webpage.")
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)
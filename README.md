# Rotten Tomatoes


# Rotten Tomatoes Top Movies Scraper

This Python script scrapes the **Top 300 Movies of All Time** from the Rotten Tomatoes editorial website. It collects movie details such as the title, director, release year, and audience score, and saves the data into a CSV file. 

---

## Prerequisites

Before running this script, ensure you have the following libraries installed in your Python environment:

1. **`requests`**: To send HTTP requests and fetch HTML content from the website.
2. **`beautifulsoup4`**: To parse and navigate through the HTML content of the webpage.
3. **`pandas`**: To create a structured DataFrame and save it to a CSV file.

Install the required libraries with:

```bash
pip install requests beautifulsoup4 pandas
```

---

## Line-by-Line Code Explanation

### Step 1: Importing Required Libraries

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

- **`requests`**: Used to make HTTP requests to the Rotten Tomatoes website.
- **`BeautifulSoup`**: Part of the `bs4` library, it helps parse and extract specific elements from the HTML content.
- **`pandas`**: Provides powerful tools for data manipulation and exporting to a CSV file.

---

### Step 2: Declaring Empty Lists

```python
Movies = []
Director = []
Year_Release = []
Liked_percentage = []
```

These empty lists will store the scraped data for:

- **`Movies`**: The names of the movies.
- **`Director`**: The names of the directors.
- **`Year_Release`**: The release years of the movies.
- **`Liked_percentage`**: Audience ratings in percentage.

---

### Step 3: Setting the Base URL and Sending the Request

```python
url = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"
r = requests.get(url)
```

- **`url`**: The Rotten Tomatoes webpage containing the list of the best movies.
- **`requests.get(url)`**: Sends a GET request to the specified URL and stores the HTML content in the variable `r`.

---

### Step 4: Parsing the HTML Content

```python
soup = BeautifulSoup(r.text, "html.parser")
```

- **`BeautifulSoup(r.text, "html.parser")`**: Parses the HTML content of the webpage into a structured format, making it easier to extract specific elements.

---

### Step 5: Scraping Data Across Pages

```python
for i in range(1, 3):
```

- **`range(1, 3)`**: Assumes there are multiple pages to scrape. This loop iterates through pages to gather all the movies. However, in this case, the page navigation logic isn't implemented correctly.

#### Handling Next Page Links

```python
np = soup.find("a", class_="post-page-numbers")
```

- **`find("a", class_="post-page-numbers")`**: Searches for the "Next Page" button in the HTML. If found, it extracts the link to the next page.

---

### Step 6: Extracting Movie Details

#### Scraping Movie Names

```python
n = soup.find_all("h2")
for i in n:
    names = i.find("a")
    if names:
        Movies.append(names.text.strip())
        Movies = Movies[:301]
```

- **`find_all("h2")`**: Locates all `<h2>` tags where movie names are stored.
- **`find("a")`**: Extracts the hyperlink tag inside the `<h2>` containing the movie name.
- **`append(names.text.strip())`**: Adds the cleaned movie name to the `Movies` list.
- **`Movies = Movies[:301]`**: Limits the list to 300 entries.

---

#### Scraping Release Years

```python
a = soup.find_all("span", class_="subtle start-year")
for j in a:
    year = j.text.strip()
    Year_Release.append(year)
    Year_Release = Year_Release[:301]
```

- **`find_all("span", class_="subtle start-year")`**: Finds all `<span>` tags with the class `"subtle start-year"`, which contain release years.
- **`append(year)`**: Adds the release year to the `Year_Release` list.

---

#### Scraping Audience Ratings

```python
b = soup.find_all("span", class_="tMeterScore")
for k in b:
    rating = k.text.strip()
    Liked_percentage.append(rating)
    Liked_percentage = Liked_percentage[:301]
```

- **`find_all("span", class_="tMeterScore")`**: Finds all `<span>` tags with the class `"tMeterScore"`, which contain audience ratings.
- **`append(rating)`**: Adds the rating to the `Liked_percentage` list.

---

#### Scraping Director Names

```python
c = soup.find_all("div", class_="info director")
for l in c:
    D = l.find("a")
    if c:
        Director.append(D.text.strip())
    Director = Director[:301]
```

- **`find_all("div", class_="info director")`**: Finds all `<div>` tags with the class `"info director"`, which contain director information.
- **`append(D.text.strip())`**: Adds the director's name to the `Director` list.

---

### Step 7: Creating a DataFrame and Saving to CSV

```python
df = pd.DataFrame({
    "Movie_name": Movies,
    "Year": Year_Release,
    "Rating(%)": Liked_percentage,
    "Directed By": Director
})
```

- **`pd.DataFrame`**: Combines the lists into a structured tabular format.
- **Column Names**:
  - `"Movie_name"`: Movie titles.
  - `"Year"`: Release years.
  - `"Rating(%)"`: Audience ratings.
  - `"Directed By"`: Director names.

---

### Step 8: Saving the Data to CSV

```python
df.to_csv("Rotten Tomatoes.csv", index=False)
```

- **`to_csv`**: Saves the DataFrame into a CSV file named `Rotten Tomatoes.csv`.
- **`index=False`**: Prevents pandas from writing the DataFrame index to the file.

---

## Running the Script

Save the script in a file (e.g., `rottentomatoes_scraper.py`) and run it:

```bash
main.py
```

The script will generate a CSV file `Rotten Tomatoes.csv` containing the scraped data.

---



## Output

The exact output of the script will depend on the current structure and data on the Rotten Tomatoes website when the script is executed. If the website structure matches the assumptions in the script, the output will be a CSV file named `Rotten Tomatoes.csv`, containing the following columns:

### Sample Output (First Few Rows)

| Movie_name                  | Year | Rating(%) | Directed By       |
|-----------------------------|------|-----------|-------------------|
| The Godfather              | 1972 | 98%       | Francis Ford Coppola |
| Citizen Kane               | 1941 | 99%       | Orson Welles      |
| Casablanca                 | 1942 | 97%       | Michael Curtiz    |
| Schindler's List           | 1993 | 98%       | Steven Spielberg  |
| The Shawshank Redemption   | 1994 | 98%       | Frank Darabont    |

### CSV File Content
The script will generate a CSV file with the following structure:

```csv
Movie_name,Year,Rating(%),Directed By
The Godfather,1972,98%,Francis Ford Coppola
Citizen Kane,1941,99%,Orson Welles
Casablanca,1942,97%,Michael Curtiz
Schindler's List,1993,98%,Steven Spielberg
The Shawshank Redemption,1994,98%,Frank Darabont
...
```

### Note:
If the script is unable to scrape data properly due to website changes, you might encounter incomplete or incorrect results. In that case, review and adjust the HTML tag and class names used in the script.
The final CSV will contain up to 300 entries if the data extraction is successful.

--------

Enjoy analyzing the data! 🎥

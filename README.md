# Rotten Tomatoes

# Rotten Tomatoes Movie Scraper

This Python script scrapes the list of the best movies of all time from Rotten Tomatoes and stores the information in a CSV file. The scraped data includes the movie name, release year, rating percentage, and the director's name.

## Required Libraries

- `requests`: To send HTTP requests and fetch web pages.
- `BeautifulSoup` from `bs4`: To parse and extract data from HTML.
- `pandas`: To store and manage the scraped data in a tabular format.

## How to Run the Code

1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

2. Run the script in your Python environment:
   ```bash
   python movie_scraper.py
   ```

3. After execution, a CSV file named `Rotten Tomatoes.csv` will be created in your working directory containing the movie information.

## Code Explanation

### Import Libraries

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

- **requests**: Used to fetch the content of the webpage.
- **BeautifulSoup**: Used to parse the HTML of the page.
- **pandas**: Used to store and manipulate the data in a structured format.

### Initialize Empty Lists for Storing Data

```python
Movies = []
Director = []
Year_Release = []
Liked_percentage = []
```

These lists will store the scraped data for each movie. We'll later use these to create a DataFrame.

### Set the URL of the Webpage to Scrape

```python
url = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"
```

This URL contains the list of the best movies of all time according to Rotten Tomatoes.

### Fetch the Webpage Content

```python
r = requests.get(url)
```

- `requests.get(url)` sends an HTTP GET request to the URL and retrieves the webpage content.

### Parse the Webpage with BeautifulSoup

```python
soup = BeautifulSoup(r.text, "html.parser")
```

- `BeautifulSoup(r.text, "html.parser")` parses the HTML content and makes it easier to extract data.

### Loop to Handle Multiple Pages (Pagination)

```python
for i in range(1, 3):
    np = soup.find("a", class_="post-page-numbers")
```

- This loop is used to navigate through multiple pages of the list. The loop goes from page 1 to page 2.

### Check if the Next Page Link Exists

```python
if np:
    npl = np["href"]
```

- We check for the link to the next page using the class `post-page-numbers` and update the URL to the new page.

### Scrape Movie Names

```python
n = soup.find_all("h2")
for i in n:
    names = i.find("a")
    if names:
        Movies.append(names.text.strip())
```

- `soup.find_all("h2")` looks for all `<h2>` elements that contain the movie names.
- We extract the text and remove any extra spaces using `.strip()`.

### Scrape Release Year

```python
a = soup.find_all("span", class_="subtle start-year")
for j in a:
    year = j.text.strip()
    Year_Release.append(year)
```

- `soup.find_all("span", class_="subtle start-year")` searches for the span tag that contains the release year of the movies.
- We extract and clean the data in a similar manner to the movie names.

### Scrape Movie Ratings

```python
b = soup.find_all("span", class_="tMeterScore")
for k in b:
    rating = k.text.strip()
    Liked_percentage.append(rating)
```

- `soup.find_all("span", class_="tMeterScore")` searches for the span tag that holds the rating percentage of the movie.
- We extract and clean the rating text.

### Scrape Director Names

```python
c = soup.find_all("div", class_="info director")
for l in c:
    D = l.find("a")
    if c:
        Director.append(D.text.strip())
```

- `soup.find_all("div", class_="info director")` searches for the div tag that contains the movie director information.
- We extract the director's name.

### Limit Data to First 300 Movies

```python
Movies = Movies[:301]
Year_Release = Year_Release[:301]
Liked_percentage = Liked_percentage[:301]
Director = Director[:301]
```

- These lines ensure that only the first 300 movies are added to the lists, even if the webpage contains more than 300 entries.

### Store the Data in a DataFrame and Save to CSV

```python
df = pd.DataFrame({"Movie_name": Movies, "Year": Year_Release, "Rating(%)": Liked_percentage, "Directed By": Director})
df.to_csv("Rotten Tomatoes.csv")
```

- We create a `pandas` DataFrame from the lists.
- The DataFrame is then saved as a CSV file named `Rotten Tomatoes.csv`.

## Final Notes

- The script scrapes data from the first two pages of the Rotten Tomatoes "Best Movies of All Time" list.
- If you want to scrape more pages, you can adjust the loop range (`range(1, 3)`).
- Make sure to respect the website's `robots.txt` file and scraping guidelines when running this script.







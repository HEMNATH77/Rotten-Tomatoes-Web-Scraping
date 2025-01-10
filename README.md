# Rotten-Tomatoes-Web-Scraping
# Rotten Tomatoes Best Movies Scraper

This project is a Python-based web scraper that extracts information about the best movies of all time from the Rotten Tomatoes website. It uses libraries like `requests`, `BeautifulSoup`, and `pandas` to scrape and store movie data in a CSV file.

---

## Features

The scraper collects the following details for up to 301 movies:  
- **Movie Name**  
- **Year of Release**  
- **Liked Percentage** (Rotten Tomatoes Score)  
- **Director Name**  

The extracted data is saved in a CSV file named `Rotten Tomatoes.csv`.

---

## Prerequisites

Make sure you have Python installed on your system. You'll also need the following Python libraries:

- `requests`
- `BeautifulSoup` (from `bs4`)
- `pandas`

Install these libraries using the following command:

```bash
pip install requests beautifulsoup4 pandas
```

---

## How to Run the Scraper

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rotten-tomatoes-scraper.git
   cd rotten-tomatoes-scraper
   ```

2. Run the Python script:
   ```bash
   python main.py
   ```

3. After execution, the extracted data will be saved in `Rotten Tomatoes.csv`.

---

## Code Overview

### Steps in the Script:

1. **Initialize Lists**:
   - Four lists (`Movies`, `Director`, `Year_Release`, and `Liked_percentage`) store the scraped data temporarily.

2. **Set the Base URL**:
   - URL for the Rotten Tomatoes page is initialized.

3. **Scraping Logic**:
   - The script fetches multiple pages using the `post-page-numbers` link for pagination.
   - For each page, it extracts:
     - Movie names from `<h2>` tags.
     - Release years from `<span>` with class `subtle start-year`.
     - Ratings from `<span>` with class `tMeterScore`.
     - Directors from `<div>` with class `info director`.

4. **DataFrame Creation**:
   - The collected data is stored in a `pandas` DataFrame and saved as a CSV file.

---

## Example Output

Below is an example of how the `Rotten Tomatoes.csv` file looks:

| Movie Name             | Year | Rating(%) | Directed By          |
|-------------------------|------|-----------|----------------------|
| The Godfather          | 1972 | 98%       | Francis Ford Coppola |
| Citizen Kane           | 1941 | 99%       | Orson Welles         |
| ...                    | ...  | ...       | ...                  |

---

## Limitations and Improvements

- **Dynamic Content**: If Rotten Tomatoes changes its HTML structure, the scraper might fail.  
- **Error Handling**: Add more robust error handling for missing or unexpected data.  
- **Pagination Limit**: Currently, it fetches up to 301 movies, which can be increased by modifying the script.

---

## Contributions

Feel free to submit pull requests or issues for any bugs or enhancements! Contributions are always welcome.  

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


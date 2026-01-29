from time import sleep
import json
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


SEARCH_URL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

RESULT_LI = 'li[data-test-id="searchResultItem"]'
TITLE = 'h3.cp-title span.title-content'
AUTHORS = 'a.author-link'
FORMAT_YEAR_DIV = 'div.cp-format-info'
FORMAT_YEAR_SPAN = 'span.display-info-primary'


def build_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )


def safe_text(parent, selector):
    try:
        return parent.find_element(By.CSS_SELECTOR, selector).text.strip()
    except NoSuchElementException:
        return ""


def main():
    driver = build_driver(headless=True)
    try:
        driver.get(SEARCH_URL)
        sleep(2)

        items = driver.find_elements(By.CSS_SELECTOR, RESULT_LI)
        print(len(items))

        results = []

        for li in items:
            title = safe_text(li, TITLE)

            author_els = li.find_elements(By.CSS_SELECTOR, AUTHORS)
            authors = "; ".join([a.text.strip() for a in author_els if a.text.strip()])

            try:
                fy_div = li.find_element(By.CSS_SELECTOR, FORMAT_YEAR_DIV)
                format_year = safe_text(fy_div, FORMAT_YEAR_SPAN)
            except NoSuchElementException:
                format_year = ""

            results.append(
                {
                    "Title": title,
                    "Author": authors,
                    "Format-Year": format_year,
                }
            )

        df = pd.DataFrame(results)
        print(df)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()

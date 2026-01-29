from time import sleep
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = "https://owasp.org/Top10/2025/"
OUT_CSV = "owasp_top_10.csv"

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


def main():
    driver = build_driver(headless=True)

    try:
        driver.get(URL)
        sleep(2)
        link_elements = driver.find_elements(
            By.XPATH,
            "//h3[contains(normalize-space(), 'Top 10:2025 List')]/following-sibling::ol[1]//a"
        )


        results = []
        for a in link_elements[:10]:
            title = a.text.strip()
            href = a.get_attribute("href")
            if title and href:
                results.append({"title": title, "href": href})

        print(results)
        with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "href"])
            for row in results:
                writer.writerow([row["title"], row["href"]])

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

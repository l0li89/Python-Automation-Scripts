from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys


class AutoExtractionApplication:

    application_path = os.path.dirname(sys.executable)
    now = datetime.now()
    date = now.strftime("%m%d%Y")
    Alzazeera = 'https://www.aljazeera.com/'
    path = 'chromedriver.exe'

    #headless-mode
    options = Options()
    options.headless = True

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Alzazeera)

    containers = driver.find_elements(by="xpath", value='//*[@id="most-read-container"]/div/ul/li')

    titles = []
    links = []

    for container in containers:
        title = container.find_element(by="xpath", value=".//article/div/h3").text
        link = container.find_element(by="xpath", value=""
                ".//article/div/h3/a[@class='article-trending__title-link u-clickable-card__link']").get_attribute("href")
        titles.append(title)
        links.append(link)

    data_dictionary = {
        'Titles': titles,
        'Links': links
    }

    file_name = f"News{date}.csv"
    final_path = os.path.join(application_path, file_name)
    data = pd.DataFrame(data_dictionary)
    data.to_csv(final_path)
    print(data_dictionary)
    driver.quit()

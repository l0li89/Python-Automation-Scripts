from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


class AutomateNewsAljazeera:
    Alzazeera = 'https://www.aljazeera.com/'
    path = 'chromedriver.exe'

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
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

    data = pd.DataFrame(data_dictionary)
    data.to_csv("AutomateNewsAljazeera.csv")
    print(data_dictionary)
    driver.quit()

import bs4 as soup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

# Initialising options for downloading
site = "http://1.186.28.31/MIT/Question%20Paper.aspx"
years = [2015, 2016, 2017, 2018]
timeline = ["Jun "]

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(site)


def search(finishedYears):
    # Resetting the state of the web page to beginning
    driver.get(site)
    year = driver.find_elements_by_xpath("//a")
    for yearElement in year:
        try:
            if int(yearElement.text) in list(set(years) - set(finishedYears)):
                currentYear = yearElement.text
                yearElement.click()
                seasons = driver.find_elements_by_xpath("//a")
                for seasonElement in seasons:
                    if "jun" in str(seasonElement.text).lower():
                        seasonElement.click()
                        sems = driver.find_elements_by_xpath("//a")
                        for semElement in sems:
                            if semElement.text == " IV Sem":
                                semElement.click()
                                branches = driver.find_elements_by_xpath("//a")
                                for branchElement in branches:
                                    if "information" in str(branchElement.text).lower():
                                        branchElement.click()
                                        papers = driver.find_elements_by_xpath("//a")
                                        print("Downloading papers for:" + currentYear)
                                        for paperElement in papers:
                                            if "systems" in str(paperElement.text).lower():
                                                urllib.request.urlretrieve(paperElement.get_attribute("href"),
                                                                           "/Users/isham/QuestionPapers/CN/" + str(
                                                                               currentYear).strip() + "_" + str(
                                                                               paperElement.text))
                                                print(paperElement.text)
                                        print("\n")
                                        search(list(set(finishedYears).union({int(currentYear)})))
                                        return

        except ValueError:
            continue


search([])

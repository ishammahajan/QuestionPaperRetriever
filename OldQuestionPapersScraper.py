import bs4 as soup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

# Initialising options for downloading
years = [2016, 2017, 2018]
timeline = ["Jun "]

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://1.186.28.31/MIT/Question%20Paper.aspx")
# driver.find_element_by_id("ctl00_ctl00_chmain_MITContent_FileGridCS_gvFiles_ctl14_lbFolderItem").click()
yearElements = driver.find_elements_by_xpath("//a")
for yearElement in yearElements:
    try:
        if int(yearElement.text) in years:
            year = yearElement.text
            yearElement.click()
            seasonElements = driver.find_elements_by_xpath("//a")
            for seasonElement in seasonElements:
                if seasonElement.text == (" Jun" + year):
                    seasonElement.click()
                    semElements = driver.find_elements_by_xpath("//a")
                    for semElement in semElements:
                        if semElement.text == " IV Sem":
                            semElement.click()
                            print(semElement.text)
            driver.back()
            print(year)
    except ValueError:
        continue
print(driver.title)


# urllib.request.urlretrieve("http://1.186.28.31/RootFolder/2018/June%202018/IV%20Sem/Information%20and%20Communication%20Technology%20Eng/Computer%20Organization%20and%20Microprocessor%20System%20(ICT%202202)%20RCS.pdf", "test.pdf")

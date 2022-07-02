from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:\\Users\\user\\dev\\covid'}
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://covid.saude.gov.br/")
driver.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button').click()
input('Espere')
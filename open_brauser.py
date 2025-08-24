from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открытие сайта
driver.get("https://itcareerhub.de/ru")

about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
about_link.click()
sleep(3)
driver.save_screenshot("./itcareerhub_screenshot_firefox.png")

sleep(5)
driver.quit()

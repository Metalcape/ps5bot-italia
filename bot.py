import json

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

def main():
    config = dict()
    with open("config.json", 'r') as infile:
        config = json.load(infile)

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.it")
    driver.find_element(By.ID, "sp-cc-accept").click()   # accept cookies

    # login
    driver.find_element(By.ID, "nav-link-accountList").click()
    driver.find_element(By.ID, "ap_email").send_keys(config["amazon"]["email"])
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "ap_password").send_keys(config["amazon"]["pass"])
    driver.find_element(By.ID, "signInSubmit").click()

    driver.get("https://www.amazon.it/dp/B08KKJ37F7")
    driver.implicitly_wait(1)   # to refresh every second
    while(True):
        if len(driver.find_elements(By.ID, "buy-now-button")) > 0:
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "buy-now-button").click()
            
            # Payment method
            driver.find_element(By.XPATH, '//input[@type="radio"][' + str(config["amazon"]["method"]) + ']').click()

            # Verify card if needed
            verify_box = driver.find_element(By.XPATH, '//input[@type="text"]')
            if verify_box.is_displayed():
                verify_box.send_keys(config["credit_card"]["number"])
                driver.find_element(By.XPATH, '//button[text()="Verifica la carta"]').click()
            driver.find_element(By.XPATH, '//input[@name="ppw-widgetEvent:SetPaymentPlanSelectContinueEvent"][1]').click()

            # BUY
            driver.find_element(By.XPATH, '//*[@id="placeYourOrder"]/span/input').click()
            driver.close()           
        else:
            driver.refresh()

if __name__ == "__main__":
    main()
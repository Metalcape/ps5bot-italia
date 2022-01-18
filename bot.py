from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.amazon.it/dp/B08KKJ37F7")

if __name__ == "__main__":
    main()
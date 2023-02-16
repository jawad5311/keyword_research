

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Web driver manager imports
from webdriver_manager.chrome import ChromeDriverManager

# Builtin Modules
import time


class KeywordResearch():
    def __init__(self):
        # Downloading driver
        self.driver_path = ChromeDriverManager().install()

        # Selenium Webdriver Options settings
        self.chr_options = Options()
        self.chr_options.add_experimental_option("detach", True)
        self.driver = self.start_driver()

    def start_driver(self):
        web_driver = webdriver.Chrome(self.driver_path,
                                      options=self.chr_options)
        return web_driver

    def test_webdriver(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_box.send_keys('test')

    def do_keyword_research_on_google(self, keyword):
        self.driver.get("https://www.google.com")

        # google search box
        search_box = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        search_box.send_keys(f'{keyword} ')

        time.sleep(2)

        suggested_keywords = self.driver.find_element(By.XPATH, "//div[@class='OBMEnb']/ul")
        print(len(suggested_keywords.find_elements(By.TAG_NAME, 'li')))

        for word in suggested_keywords.find_elements(By.TAG_NAME, 'li'):
            print(word.text)







if __name__ == "__main__":
    driver = KeywordResearch()
    # driver.test_webdriver()

    driver.do_keyword_research_on_google()

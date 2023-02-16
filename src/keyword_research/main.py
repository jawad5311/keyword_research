

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Web driver manager imports
from webdriver_manager.chrome import ChromeDriverManager


# Selenium Webdriver Options settings
chr_options = Options()
chr_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome('../../chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          options=chr_options)

driver.get("https://www.google.com")









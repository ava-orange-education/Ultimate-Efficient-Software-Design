from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Navigate to a website
driver.get("http://www.example.com")

# Find an element and perform actions
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

# Close the browser
driver.quit()

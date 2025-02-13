import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Set the desired window size for 2K resolution
driver.set_window_size(2560, 1440)

# Open the webpage
driver.get("https://meshmap.iowamesh.net/?lat=41.9953615365105&lng=267.2328359397183&zoom=9")

# Wait for the page to load completely
time.sleep(5)  # Adjust the sleep time if necessary

# Try to close the pop-up if it exists
try:
    pop_up = driver.find_element(By.CSS_SELECTOR, "div.bg-gray-100.hover:bg-gray-200.p-2.rounded-full")
    anchor_tag = pop_up.find_element(By.XPATH, "..")  # Find the parent <a> tag
    anchor_tag.click()
except (NoSuchElementException, ElementClickInterceptedException) as e:
    print(f"Pop-up not found or could not be clicked: {e}")

# Create the screenshots directory if it doesn't exist
screenshots_dir = "screenshots"
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

# Generate the filename with date and time stamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")

# Take a screenshot and save it to the output file
driver.save_screenshot(filename)

# Close the browser
driver.quit()

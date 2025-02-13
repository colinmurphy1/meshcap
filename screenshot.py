import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the webpage
driver.get("https://meshmap.iowamesh.net/?lat=41.9953615365105&lng=267.2328359397183&zoom=9")

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

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Wait for the element to be present and get its location
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-7:nth-child(1) path:nth-child(3)"))
    )
    location = close_button.location
    print("Close button location:", location)
    
    # Use JavaScript to simulate a click event at the specified coordinates
    driver.execute_script(f"document.elementFromPoint({location['x']}, {location['y']}).click();")
except Exception as e:
    print("Close button not found or could not be clicked:", e)

# Create the screenshots directory if it doesn't exist
screenshots_dir = "screenshots"
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

# Generate the
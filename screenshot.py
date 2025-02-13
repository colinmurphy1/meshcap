import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Required for Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Helps prevent crashes
chrome_options.add_argument("--window-size=1920x1080")  # Set window size

# Path to ChromeDriver inside the container
chrome_driver_path = "/usr/bin/chromium-driver"

# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to open
url = "https://meshmap.iowamesh.net/?lat=42.03193413223133&lng=266.5022277832032&zoom=10"
driver.get(url)

# Generate timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
screenshot_filename = f"screenshots/screenshot_{timestamp}.png"

# Ensure screenshots directory exists
os.makedirs("screenshots", exist_ok=True)

# Save screenshot
driver.save_screenshot(screenshot_filename)

print(f"Screenshot saved: {screenshot_filename}")

# Close the browser
driver.quit()

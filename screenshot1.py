

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time

# options = Options()
# options.add_argument("--start-maximized")  
# # ChromeDriverManager().install() → Automatically downloads the correct ChromeDriver.
# # WebDriverWait(driver, 10) #→ Waits up to 10 seconds for page elements to appear

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# url = "http://127.0.0.1:5000"
# driver.get(url)
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "top")))

# #Wait until there is an element on the page with the HTML id = top.
# # So Selenium keeps checking for up to 10 seconds — as soon as it finds that element, it proceeds

# folder = "Pictures"
# os.makedirs(folder, exist_ok=True)

# timestamp = time.strftime("%Y%m%d-%H%M%S")#This line gets the current date and time and formats it neatly
# filename = f"{folder}/Blog_{timestamp}.png"

# driver.save_screenshot("Screenshot.png")
# print(f"✅ Screenshot saved: {filename}")

# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import datetime

def take_screenshot():
    # --- Config ---
    URL = " http://127.0.0.1:5000/"  # Your mini-blog URL
    SAVE_FOLDER = "Pictures"

    # Create folder if it doesn't exist
    os.makedirs(SAVE_FOLDER, exist_ok=True)

    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximize")  # Run browser in background
    chrome_options.add_argument("--window-size=1920,1080")

    # Automatically install and use ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(URL)
        time.sleep(3)  # wait for page to load

        # Save screenshot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(SAVE_FOLDER, f"dashboard_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
    finally:
        driver.quit()

# Run script directly
if __name__ == "__main__":
    take_screenshot()
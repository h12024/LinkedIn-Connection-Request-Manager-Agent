from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Credentials
LINKEDIN_USERNAME = "username"
LINKEDIN_PASSWORD = "password"

# Setup
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

try:
    # 1. Login
    driver.get("https://www.linkedin.com/login")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(LINKEDIN_USERNAME)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("✅ Logged in.")
    time.sleep(3)

    # 2. Go to Grow tab
    driver.get("https://www.linkedin.com/mynetwork/grow/")
    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Invitations')]")))
    print("📍 On Grow page.")
    time.sleep(5)

    # 3. Accept all invitations
    while True:
        accept_buttons = driver.find_elements(By.XPATH, "//button[normalize-space()='Accept']")
        print(f"👉 Found {len(accept_buttons)} Accept button(s).")

        if not accept_buttons:
            print("✅ All requests accepted or none found.")
            break

        for button in accept_buttons:
            try:
                driver.execute_script("arguments[0].click();", button)
                print("👍 Accepted one invitation.")
                time.sleep(2)
            except Exception as e:
                print(f"❌ Error clicking Accept: {e}")
        time.sleep(2)  # Let UI update

except Exception as e:
    print(f"💥 Error: {e}")

finally:
    print("🛑 Closing browser in 5 seconds.")
    time.sleep(5)
    driver.quit()

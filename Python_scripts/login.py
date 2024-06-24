import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_hugging_face(driver, username, password):
    driver.get("https://huggingface.co/login")
    
    try:
        # Wait for the username and send username
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(username)
        
        # Wait for the password and send password
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)
        
        # Click login button
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()
        
        # Wait for a successful login
        time.sleep(5)
        
        print("Logged in successfully!")
        
    except Exception as e:
        print(f"Error during login: {e}")
        print(driver.page_source)
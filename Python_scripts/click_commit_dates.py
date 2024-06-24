import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def get_commit_dates(driver, link):
    try:
        # Wait for commit dates
        commit_dates = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//time[@datetime]"))
        )
        latest_commit_date = commit_dates[0].get_attribute('datetime')
        
        # Try to go to last page
        while True:
            try:
                next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
                next_button.click()
                time.sleep(2)
            except:
                break
        
        commit_dates = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//time[@datetime]"))
        )
        oldest_commit_date = commit_dates[-1].get_attribute('datetime')
        
        return latest_commit_date, oldest_commit_date
    except Exception as e:
        print(f"Error extracting commit dates: for {link}") # {e}")
        return None, None

def click_files_and_versions(driver, link):
    driver.get(link)
    try:
        # Click on "Files and versions"
        files_and_versions_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[.//span[contains(text(), 'Files and versions')]]"))
        )
        files_and_versions_tab.click()

        # Extract no. of commits
        commits_info = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[.//span[contains(text(), 'commits')]]"))
        )
        commits_text = commits_info.text
        number_of_commits = int(re.search(r'\d+', commits_text).group())

        # Click "commits"
        commits_info.click()

        # Extract latest and oldest commit dates
        latest_commit_date, oldest_commit_date = get_commit_dates(driver, link)
        
        return number_of_commits, latest_commit_date, oldest_commit_date
        
    except Exception as e:
        print(f"Error navigating to 'Files and versions' or 'commits' for {link}") # : {e}")
        return None, None, None

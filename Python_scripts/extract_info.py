import json
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_info(driver, link):
    driver.get(link)
    try:
        # Wait for data-props attribute
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-target='InferenceWidget']"))
        )
        data_props = element.get_attribute('data-props')
        data = json.loads(data_props)
        downloads_all_time = data['model']['downloadsAllTime']


        # Check for Arxiv tag
        tags = data['model'].get('tags', [])
        has_arxiv = any(re.match(r'arxiv:\d+\.\d+', tag) for tag in tags)
        
        # Check for "No model card" text
        try:
            no_model_card_element = driver.find_element(By.XPATH, "//p[contains(text(), 'No model card')]")
            model_card = 0
        except:
            model_card = 1
        
        return downloads_all_time, int(has_arxiv), model_card
    except Exception as e:
        print(f"Error extracting info for {link}")
        return None, None, None

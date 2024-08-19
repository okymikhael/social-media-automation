from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import logging

load_dotenv()

unfollow_count = int(os.getenv('UNFOLLOW_COUNT', 100))
wait_time = int(os.getenv('WAIT_TIME', 4500))

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

user_data_dir = os.path.expanduser('~') + '/Library/Application Support/Google/Chrome'  # macOS base path
profile_directory = "Default"
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_directory}")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

logger.info(f"Using Chrome profile: {profile_directory}")
logger.info(f"User data directory: {user_data_dir}")

def main():
    try:
        logger.info("Initializing Chrome driver...")
        driver = webdriver.Chrome(options=chrome_options)
        logger.info("Chrome driver initialized successfully.")
        
        logger.info("Navigating to Instagram...")
        driver.get("https://www.instagram.com")
        
        logger.info("Waiting for page to load...")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        logger.info(f"Navigated to Instagram. Current URL: {driver.current_url}")
        
        # Check if we're logged in
        if "accounts/login" not in driver.current_url:
            logger.info("Already logged in to Instagram.")
        else:
            logger.warning("Not logged in. You may need to log in manually.")
        
        # Click on the specified element
        logger.info("Attempting to click on the specified element...")
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[8]/div/span/div/a/div")))
            element.click()
            logger.info("Successfully clicked on the element.")
        except Exception as e:
            logger.error(f"Failed to click on the element: {str(e)}")
            raise

        # Click on the followers link
        logger.info("Attempting to click on the followers link...")
        try:
            followers_element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a")))
            followers_element.click()
            logger.info("Successfully clicked on the followers link.")
        except Exception as e:
            logger.error(f"Failed to click on the followers link: {str(e)}")
            raise
        
        # Wait for the followers modal to load
        logger.info("Waiting for the followers modal to load...")
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))
            logger.info("Followers modal loaded successfully.")
        except Exception as e:
            logger.error(f"Followers modal did not load: {str(e)}")
            raise
        
        unfollow_process(driver, wait)
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

    finally:
        if 'driver' in locals():
            logger.info("Closing Chrome driver...")
            driver.quit()
            logger.info("Chrome driver closed.")

def unfollow_process(driver, wait):
    # Initialize counter for unfollowed accounts
    unfollowed_count = 0

    while True:
        # Loop to unfollow 100 accounts
        for i in range(1, unfollow_count + 1):
            try:
                # Construct the XPath for the unfollow button using the loop variable
                unfollow_xpath = f"/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button"

                # Wait for the unfollow button to be clickable
                unfollow_button = wait.until(EC.element_to_be_clickable((By.XPATH, unfollow_xpath)))
                
                # Click the unfollow button
                unfollow_button.click()
                
                # Wait for the confirmation dialog to appear
                logger.info("Waiting for the unfollow confirmation dialog...")
                try:
                    confirm_unfollow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]")))
                    # Click the confirm unfollow button
                    confirm_unfollow_button.click()
                    logger.info("Confirmed unfollow action.")
                except Exception as e:
                    logger.warning(f"Failed to confirm unfollow: {str(e)}")
                    # If we can't find the confirmation button, we'll continue with the next account
                    continue
                
                # Wait for a short time to allow the unfollow action to complete
                time.sleep(1)
                
                # Increment the counter
                unfollowed_count += 1
                
                logger.info(f"Unfollowed account {unfollowed_count}")
                
                # Optional: Add a short delay between unfollows to avoid rate limiting
                time.sleep(2)
                
            except Exception as e:
                logger.warning(f"Failed to unfollow account {i}: {str(e)}")
                # If we can't find the button, we might have reached the end of the list
                if "no such element" in str(e).lower():
                    logger.info("Reached the end of the visible list. Stopping unfollow process.")
                    break
        
        logger.info(f"Unfollowing process completed. Total accounts unfollowed: {unfollowed_count}")
        
        logger.info(f"Waiting for {wait_time} seconds before continuing...")
        time.sleep(wait_time)
        
        logger.info("Wait completed. Resuming operation...")

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_driver(search_tag):
    logger.info("Setting up Chrome driver")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    user_data_dir = os.path.expanduser('~') + '/Library/Application Support/Google/Chrome'
    profile_directory = "Default"
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    chrome_options.add_argument(f"profile-directory={profile_directory}")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Add option to save downloads to the specified directory
    download_dir = f"/Users/okymikhael/Documents/work/sandbox/cloude_code/selenium/app/video/{search_tag}/original"
    os.makedirs(download_dir, exist_ok=True)  # Create the directory if it doesn't exist
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    logger.info(f"Chrome driver setup complete. Downloads will be saved to: {download_dir}")
    return webdriver.Chrome(options=chrome_options)

def search_tiktok(driver, search_term):
    logger.info(f"Searching TikTok for: {search_term}")
    time.sleep(10)  # Wait for page to load
    driver.get(f"https://www.tiktok.com/search?q={search_term}")
    time.sleep(5)  # Wait for page to load
    logger.info("Search page loaded")

def get_video_urls(driver, num_videos=5):
    logger.info(f"Attempting to fetch {num_videos} video URLs")
    video_urls = []
    wait = WebDriverWait(driver, 10)
    
    try:
        # Find all img elements inside the specified div
        img_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div//img")))
        logger.info(f"Found {len(img_elements)} img elements")
        
        # Scroll to load more videos if needed
        while len(img_elements) < num_videos:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new content to load
            
            # Re-fetch img elements
            img_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div//img")

            # Check if we've reached the end of the page
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if new_height == last_height:
                logger.info("Reached the end of the page")
                break
        
        logger.info(f"Found {len(img_elements)} img elements after scrolling")
        
        for index, img in enumerate(img_elements):
            if len(video_urls) >= num_videos:
                break
            
            logger.info(f"Looping num: {index}")
            
            try:
                video_element = driver.find_element(By.XPATH, f'//*[@id="tabs-0-panel-search_top"]/div/div/div[{index + 1}]/div[1]/div/div/a')
                video_src = video_element.get_attribute('href')
                
                if video_src and video_src not in video_urls:
                    video_urls.append(video_src)
                    logger.info(f"Found video URL: {video_src}")
            except Exception as e:
                logger.warning(f"Failed to get video source: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error while getting video URLs: {str(e)}")
    
    return video_urls[:num_videos]

def download_video(driver, uri):
    logger.info(f"Attempting to download video from: {uri}")
    try:
        # Open a new tab and navigate to SnapTik.app
        driver.execute_script("window.open('https://snaptik.app', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        
        for url in uri:
            # Wait for the input field to be present
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/div/form/div[2]/input[1]"))
            )
            
            # Input the video URL
            input_field.clear()  # Clear any existing text
            input_field.send_keys(url)
            
            # Submit the form
            submit_button = driver.find_element(By.XPATH, "/html/body/section[1]/div/form/button")
            submit_button.click()
            
            # Wait for the download button to appear
            download_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div[2]/div/div[2]/a[1]"))
            )
            
            # Click the download button
            download_button.click()
            
            # Wait for the download to complete (you may need to adjust this time)
            
            logger.info(f"Video downloaded from {url} successfully")
            
            # Check if the "Download Another Video" button is present
            try:
                home_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div[2]/div/div[2]/a[2]"))
                )
                home_button.click()
                # If the button is clicked successfully, continue the loop
                continue
            except:
                # If the button is not found, break the loop
                break
        
        # Close the tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        # Make sure to switch back to the original tab even if an error occurs
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        
def main():
    logger.info("Starting TikTok scraper")
    search_term = input("Enter the TikTok search term: ")
    num_videos = int(input("Enter the number of videos to download: "))
    logger.info(f"User input: search term '{search_term}', {num_videos} videos")
    
    driver = setup_driver(search_term)
    try:
        search_tiktok(driver, search_term)
        video_urls = get_video_urls(driver, num_videos)
        download_video(driver, video_urls)
        
        logger.info(f"Downloaded {len(video_urls)} videos successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
    logger.info("TikTok scraper finished")

if __name__ == "__main__":
    main()
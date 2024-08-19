from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Facebook credentials
username = 'your_facebook_username'
password = 'your_facebook_password'

# ChromeDriver path (Update this to your chromedriver path)
driver = webdriver.Chrome(executable_path='/storage/emulated/0/Download/chromedriver')

def login_facebook():
    driver.get("https://www.facebook.com/login")
    
    username_box = driver.find_element("id", "email")
    username_box.send_keys(username)
    
    password_box = driver.find_element("id", "pass")
    password_box.send_keys(password)
    
    login_button = driver.find_element("name", "login")
    login_button.click()
    
    # Wait to simulate human behavior
    time.sleep(random.uniform(5, 10))
    
    # Random actions
    perform_random_actions()
    
    # Log out or just keep the session active
    time.sleep(random.uniform(300, 600))  # 5 to 10 minutes
    driver.quit()

def perform_random_actions():
    # Randomly perform an activity
    actions = [
        scroll_newsfeed,
        like_post,
        open_chat
    ]
    random.choice(actions)()

def scroll_newsfeed():
    body = driver.find_element("tag name", "body")
    for _ in range(random.randint(5, 10)):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(random.uniform(1, 3))

def like_post():
    like_buttons = driver.find_elements("xpath", "//div[@aria-label='Like']")
    if like_buttons:
        random.choice(like_buttons).click()

def open_chat():
    chat_buttons = driver.find_elements("xpath", "//a[contains(@href, 'messages')]")
    if chat_buttons:
        random.choice(chat_buttons).click()
        time.sleep(random.uniform(2, 5))
        driver.back()

# Loop to keep the bot running periodically
while True:
    login_facebook()
    time.sleep(random.uniform(3600, 7200))  # 1 to 2 hours before next login
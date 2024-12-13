import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def open_driver(group_name, admin_name):
    try:
        is_logged_in = False
        current_dir = os.path.dirname(os.path.abspath(__file__))
        profile_dir = os.path.join(current_dir, "wapp_profile")

        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={profile_dir}")
        chromedriver_path = "/usr/bin/chromedriver"

        # Smaller screen if no need to login
        if os.path.isdir(profile_dir):
            is_logged_in = True
            chrome_options.add_argument("--window-size=1,1")

        # # This driver for windows
        # driver = webdriver.Chrome()

        # This driver for rpi
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chromedriver_path), options=chrome_options)

        driver.get("https://web.whatsapp.com")

        if is_logged_in:
            driver.set_window_size(1, 1)
            driver.set_window_position(-2000, 0)
            driver.minimize_window()

        time.sleep(60)

        # Search for the admin
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(admin_name + Keys.ENTER)
        time.sleep(2)
        send_msg(driver, "The WhatsApp bot started.")
        time.sleep(5)

        # Search for the group
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(group_name + Keys.ENTER)
        time.sleep(2)

        return driver
    except Exception as e:
        print(f"Error open_driver(): {e}")
        return 1


def send_msg(driver, msg):
    try:
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

        # Simulate Shift + Enter for newlines
        for char in msg:
            if char == '\n':
                message_box.send_keys(Keys.SHIFT + Keys.ENTER)
            else:
                message_box.send_keys(char)

        # Send the message with Enter key
        message_box.send_keys(Keys.ENTER)
        return True
    except Exception as e:
        print(f"Error send_msg(driver, receiver, msg): {e}")
        return False


def check_new_message(driver, callback):
    try:
        first_run = True
        last_messages_count = 0

        while True:
            messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in")]')
            current_messages_count = len(messages)

            if current_messages_count > last_messages_count:
                new_messages = messages[last_messages_count:]

                if not first_run:
                    for msg_element in new_messages:
                        try:
                            callback(msg_element.find_element(By.XPATH, './/div[contains(@class, "copyable-text")]').text)
                        except Exception as e:
                            print(f"Error check_new_message(driver, callback) in message: {e}")
                else:
                    first_run = False


                last_messages_count = current_messages_count

            time.sleep(5)
    except Exception as e:
        print(f"Error check_new_message(driver, callback): {e}")

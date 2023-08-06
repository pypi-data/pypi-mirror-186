import datetime
import psycopg2
import pytesseract

import os
import requests
import zipfile
import time
import random
import undetected_chromedriver.v2 as uc

from twocaptcha import TwoCaptcha
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
DATABASE_URL="postgresql://victor:6OkPKgBQrktuaqnH2RgCzg@free-tier4.aws-us-west-2.cockroachlabs.cloud:26257/postal?sslmode=prefer&options=--cluster%3Dtundra-badger-3949"
NOPECHA_KEY = 'I-7T7KTE4NNMDU'

written = 0
goal = random.randint(50, 60)

def wait(secs=0):
    time.sleep(secs + random.random())

def solveRecaptcha(sitekey, url):
    solver = TwoCaptcha("8a587be4fe022de5e80be77f35da99ae")
    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)
    except Exception as e:
        print(e)
    else:
        return result

def login(driver, username, password):
    print("Logging in...")
    driver.get("https://globalpoker.com/")

    try:
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Log In')]")))
        login_button.click()
    except TimeoutException:
        print("Login button not found")

    try:
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'lobby-avatar')]")))
        print("Logged in already")
    except TimeoutException:
        try:
            username_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "email")))
            username_box.send_keys(username)

            password_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "password")))
            password_box.send_keys(password)

            wait(1)
            password_box.send_keys(Keys.ENTER)

            print("Logged in")
        except TimeoutException:
            print("Login boxes not found")

def close_modals(driver):
    pass
    # try:
    #     print("Finding continue button")
    #     continue_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Continue')]")))
    #     continue_button.click()
    #     print("Continue clicked")
    # except TimeoutException:
    #     print("Continue button not found")

    # try:
    #     print("Finding my stash button")
    #     my_stash_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Claim')]")))
    #     my_stash_button.click()
    #     print("My stash claimed")
    # except TimeoutException:
    #     print("My stash not found")

    # try:
    #     print("Finding daily bonus button")
    #     daily_bonus_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='styles_claimBtn___pOxw']")))
    #     daily_bonus_button.click()
    #     print("Daily bonus claimed")
    # except TimeoutException:
    #     print("Daily bonus modal not found")

    # try:
    #     print("Finding offer close button")
    #     offer_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='close-modal-button']")))
    #     offer_button.click()
    #     print("Offer closed")
    # except TimeoutException:
    #     print("Offer modal not found")

def postal(driver, username, password):
    global written

    conn = psycopg2.connect(DATABASE_URL)

    login(driver, username, password)
    close_modals(driver)
    
    while written < goal:
        close_modals(driver)
        try:
            print("Finding get coins button")
            get_coins_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cashier-button")))
            wait(2)
            get_coins_button.click()
            print("Get coins button clicked")
        except TimeoutException:
            print("Failed to find get coins button")
            # driver.save_screenshot('screenie1.png')
            raise
        
        try:
            print("Finding play for free button")
            play_for_free_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Play for Free')]")))
            wait(2)
            play_for_free_button.click()
            print("Play for free button clicked")
        except TimeoutException:
            print("Failed to find play for free button")
            # driver.save_screenshot('screenie2.png')
            raise

        while written < goal:
            try:
                print("Finding click here button")
                postal_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Click here')]")))
                wait(1)
                postal_button.click()
                print("Click here button clicked")
            except TimeoutException:
                print("Failed to find click here button")
                # driver.save_screenshot('screenie3.png')
                raise

            # wait(4)

            try:
                print("Finding IFrame")
                # iframe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "iframe")))
                # driver.switch_to.frame(iframe)
                WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='https://payments.vgwgroup.net']")))
                print("Switched to IFrame")
            except TimeoutException:
                print("Failed to find IFrame")
                # driver.save_screenshot('screenie4.png')
                raise

            # iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
            # driver.switch_to.frame(iframe)

            try:
                print("Finding postal request button")
                postal_request_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "get-postal-request-code")))
                wait(1)
                postal_request_button.click()
                print("Postal request button clicked")
            except TimeoutException:
                print("Failed to find postal request button")
                # driver.save_screenshot('screenie5.png')
                raise

            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
            except TimeoutException:
                print("Failed to find captcha")
                raise

            print("Solving captcha")
            # driver.save_screenshot('captcha1.png')
            res = solveRecaptcha(
                "6LfvyQ0iAAAAAGBPXO2PBIW1JLftMPb47T8IxORq",
                "https://payments.vgwgroup.net/"
            )
            print("Captcha solved")
            # driver.save_screenshot('captcha2.png')

            code = res["code"]

            driver.execute_script(
                "___grecaptcha_cfg.clients['0']['T']['T']['callback'](" "'" + code + "')"
            )

            prc_image = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='border: 3px solid']")))

            prc_image.screenshot("code.png")
            prc = pytesseract.image_to_string("code.png").strip()

            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO postal_codes (postal_code, casino_name, user_email, generate_time) VALUES (%s, %s, %s, now());", (prc, "gp", username)
                )
            conn.commit()
            print("Wrote new code: ", written, prc)
            written += 1

            try:
                print("Finding return button")
                return_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "return")))
                wait(2)
                return_button.click()
                print("Return button clicked")
            except TimeoutException:
                print("Failed to find return button")
                # driver.save_screenshot('screenie6.png')
                raise
            
            driver.switch_to.default_content();
            
            rand_time = random.randint(300, 420)
            cur_time = datetime.datetime.now()
            next_time = cur_time + datetime.timedelta(seconds=rand_time)
            print("Current time is ", cur_time.time(), ". Waiting until ", next_time.time())
            wait(rand_time)

def get_gp(username, password):
    global written

    options = uc.ChromeOptions()
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')

    driver = uc.Chrome(options=options, user_data_dir=f"{os.getcwd()}/profile")

    # print("Disabling NopeCHA...")
    # driver.get(f"https://nopecha.com/setup#{NOPECHA_KEY}|enabled=false")

    while written < goal:
        # login(driver, username, password)
        try:
            postal(driver, username, password)
        except Exception as e:
            print("Postal failed with error: ", e)

    driver.quit()

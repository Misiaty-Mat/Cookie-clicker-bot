from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
UPGRADE_TIMER = 3
CHROME_DRIVER = ""  # Chrome driver path


# Function created for managing upgrade system
def buy_upgrade():
    # getting all upgrade buttons
    upgrades_cost_tags = driver.find_elements(By.CSS_SELECTOR, "#store div b")

    # Getting intiger cost of each upgrade
    upgrades_cost = [
        int(upgrade.text.split()[-1].replace(",", ""))
        for upgrade in upgrades_cost_tags[:-1]
    ]

    # Importing current cookies clicked
    current_cookies_tag = driver.find_element(By.ID, "money")
    current_cookies_number = int(current_cookies_tag.text.replace(",", ""))

    # Lookig for the highes afordable upgrade
    to_buy = None
    for index, upgrade in enumerate(upgrades_cost):
        if current_cookies_number > upgrade:
            to_buy = index
        else:
            break

    # Buying upgrade
    if to_buy != None:
        upgrade_buttons = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        afordable_upgrade = upgrade_buttons[to_buy]
        afordable_upgrade.click()


# Set up timer for buying items
buy_after = time() + UPGRADE_TIMER

# Chrome driver setup
driver = webdriver.Chrome(
    executable_path=CHROME_DRIVER,
)

driver.get("https://orteil.dashnet.org/experiments/cookie/")


# Cookie to click
cookie = driver.find_element_by_id("cookie")

# Mainloop
while True:
    cookie.click()
    if time() > buy_after:
        buy_upgrade()
        buy_after = time() + UPGRADE_TIMER

import logging
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from HomePage2 import HomePage


def open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr/")
    barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("Playstation 5" + Keys.ENTER)
    time.sleep(2)

    driver.switch_to.frame("iframeResult") ## avec id ou name
    driver.switch_to.frame(0) ## avec index

    iframe = driver.find_element(By.CSS_SELECTOR, "iframe#iframeResult")
    driver.switch_to.frame(iframe) ## avec WebElement

    driver.switch_to.default_content()

    driver.quit()

def css_correction():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()

    epicerie_salee_menu = driver.find_element(By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee_menu)
    action.perform()

def carrefour():
    # Open browser and go to Web page
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    # Definition of explicit wait
    wait = WebDriverWait(driver, 10)

    # Close cookies pop up
    close_cookies = wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    click_with_log(driver, close_cookies)

    # Clic on hamburger button
    hamburger_button = driver.find_element(By.CSS_SELECTOR, "#data-rayons")
    hamburger_button.click()
    logging.debug("The button was clicked")

    # hover to epicerie salee
    epicerie_salee = wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salÃ©e']")))
    action.move_to_element(epicerie_salee)
    action.perform()


    # hover to feculent
    feculent = wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")))
    action.move_to_element(feculent)
    action.perform()

    # clic on pate
    pates = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
    pates.click()
    logging.debug("The button was clicked")

    # Call function to open product
    # openProducts(driver, 4)
    openProducts2(driver, 3)

    # Clic on buy button
    buy_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter")))
    buy_button.click()

    # Clic on Drive pick up
    pick_up = wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")))
    pick_up.click()

    # print zip code inside text box
    zip_code = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[data-cs-mask=true]")))
    zip_code.send_keys("75001")
    time.sleep(1)
    zip_code.send_keys(Keys.ENTER)

    # select first store available
    first_store = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")))
    first_store.click()

    # Control : product is not available
    add_info = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, ".missing-products .ds-body-text--color-inherit")))
    assert add_info.text == "1 produit indisponible dans ce magasin."
    timestr = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f'C:\\Users\\ib\\PycharmProjects\\A4Q\\screenshots\\capture{timestr}.png'
    driver.get_screenshot_as_file(screenshot_name)
    print("Test is PASSED !!!!")

    driver.quit()


def test_page_object():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    home = HomePage(driver)
    home.close_cookie()

    driver.quit()

def openProducts2(driver, index):
    # Function to open product by list
    if index >= 0 and index < 60:
        product_list = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) .product-card-image")
        product_list[index].click()
    else:
        print("Index value is out of range. Should be between 0 and 59")

def click_with_log(driver, web_element: WebElement):
    web_element.click()
    logging.debug("The button " + web_element.id + " was clicked")








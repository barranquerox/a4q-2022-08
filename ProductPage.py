import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:
    buy_button_selector = "#data-produit-acheter"
    pick_up_selector = ".push-services--pickers li:nth-child(1)"
    Zip_code_selector = "[data-cs-mask=true]"
    first_store_selector = ".drive-service-list__list > li:nth-child(1) button"
    Message_selector = ".ds-body-text.ds-body-text--weight-bold.ds-body-text--size-m.ds-body-text--color-inherit"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Buy
    def Buy(self):
        self.wait.until(expected_conditions.element_to_be_clickable
                        ((By.CSS_SELECTOR, self.buy_button_selector))).click()

    # ChooseDeliveryMethod
    def Choose_Delivery_Method(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, self.pick_up_selector))).click()

    #EnterZipCode()
    def Enter_Zip_Code(self):
        zip_code = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.Zip_code_selector)))
        zip_code.send_keys("75001")
        time.sleep(1)
        zip_code.send_keys(Keys.ENTER)

    #SelectFirstStore()
    def  Select_First_Store(self):
        self.wait.until(expected_conditions.element_to_be_clickable
                        ((By.CSS_SELECTOR, self.first_store_selector))).click()

    #GetAvailabilityStatus()
    def Get_Availability_Status(self):
        Message = self.wait.until(expected_conditions.visibility_of_element_located
                                  ((By.CSS_SELECTOR, self.Message_selector)))
        return Message.text
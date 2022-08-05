from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    close_cookie_button_selector = (By.ID, "onetrust-accept-btn-handler")
    hamburger_button_selector = "#data-rayons"
    epicerie_salee_selector = (".nav-item__menu-link [alt='Epicerie salée']")
    feculent_selector = "#data-menu-level-1_R12 > li:nth-child(7)"
    pates_selector = "#data-menu-level-2_R12F05 > li:nth-child(3)"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(self.driver)

    # Close cookies pop up
    def close_cookie(self):
        close_cookie_button = self.wait.until(expected_conditions.element_to_be_clickable(self.close_cookie_button_selector))
        close_cookie_button.click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.close_cookie_button_selector))

    # OpenMenu
    def Open_Menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.hamburger_button_selector).click()

    # OpenEpicerieSalee
    def Open_Epicerie_Salee(self):
        epicerie_salee = self.wait.until(expected_conditions.element_to_be_clickable
                                         ((By.CSS_SELECTOR, self.epicerie_salee_selector)))
        #action = ActionChains(self.driver)
        self.action.move_to_element(epicerie_salee)
        self.action.perform()

    # OpenSubCategoryMenu
    def Open_SubCategory_Menu(self):
        feculent = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.feculent_selector)))
        self.action.move_to_element(feculent)
        self.action.perform()

    # OpenProductCategoryPage(category)
    def Open_Product_Category_Page_category(self):
        self.driver.find_element(By.CSS_SELECTOR, self.pates_selector).click()
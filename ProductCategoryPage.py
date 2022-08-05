from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductCategoryPage:
    Liste_produits_selector = ".product-grid-item:not(.storetail) h2"


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # OpenProductPage(int)
    def OpenProductPage(self, index):
        liste_produits = self.driver.find_elements(By.CSS_SELECTOR, self.Liste_produits_selector )
        liste_produits[index].click()

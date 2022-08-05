from selenium import webdriver

from HomePage import HomePage
from ProductCategoryPage import ProductCategoryPage
from ProductPage import ProductPage

def page_object():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    home = HomePage(driver)
    home.close_cookie()
    home.Open_Menu()
    home.Open_Epicerie_Salee()
    home.Open_SubCategory_Menu()
    home.Open_Product_Category_Page_category()

    Produit = ProductCategoryPage(driver)
    Produit.OpenProductPage(3)

    Acheter = ProductPage(driver)
    Acheter.Buy()
    Acheter.Choose_Delivery_Method()
    Acheter.Enter_Zip_Code()
    Acheter.Select_First_Store()

    Message_attendu = "1 produit indisponible dans ce magasin."
    assert Acheter.Get_Availability_Status() == Message_attendu

    driver.quit()
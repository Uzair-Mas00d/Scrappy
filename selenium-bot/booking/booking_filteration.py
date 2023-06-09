from selenium.webdriver.remote.webdriver import WebDriver # for vs code to understand that we are using webdriver. it help in its intellesense(auto typing) Not important
from selenium.webdriver.common.by import By

class BookingFilteration():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self,*star_values):
        star_filtriation_box =  self.driver.find_element(By.ID,'filter_group_class_:R14q:')
        star_child_element = star_filtriation_box.find_elements(By.CSS_SELECTOR,'*')
        
        for star_value in star_values:
            for star_element in star_child_element:
                if str(star_element.get_attribute('innerHTML')).strip() == f"{star_value} stars":
                    star_element.click()
    
    def sort_price_lowest_first(self):
        filter_element_btn = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        filter_element_btn.click()

        lowest_price = self.driver.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        lowest_price.click()

from selenium.webdriver.remote.webdriver import WebDriver # for vs code to understand that we are using webdriver. it help in its intellesense(auto typing) Not important
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self,boxes_section_element:WebDriver):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes() # for use alternative name for finction

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')
    
    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CSS_SELECTOR,'div[data-testid="title"]').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]').get_attribute('innerHTML').strip()
            hotel_score = deal_box.find_elements(By.CLASS_NAME,'b5cd09854e')[0].get_attribute('innerHTML').strip()

            collection.append([hotel_name,hotel_price,hotel_score])
        
        return collection
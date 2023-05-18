import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filteration import BookingFilteration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r'E:\Scrappy\seleniumDriver'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
    
        select_currency = self.find_element(By.XPATH,f'//div[contains(text(),"{currency}")]')
        select_currency.click()
    
    def select_place(self,place):
        search_field = self.find_element(By.ID,":Ra9:")
        search_field.clear()
        search_field.send_keys(place)

        first_result = self.find_element(By.XPATH,f'//div[contains(text(),"{place}")]')
        first_result.click()

    def select_Date(self,check_in,check_out):
        check_in_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in}"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_out}"]')
        check_out_element.click()
    
    def select_adults(self,count=1):
        selection_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
        selection_element.click()

        while True:
            decrese_adult_element = self.find_elements(By.CLASS_NAME, 'b9def0936d')
            decrese_adult_element[1].click()
            adult_value_element = self.find_element(By.ID,'group_adults')
            adult_value =  adult_value_element.get_attribute('value')

            if int(adult_value) == 1:
                break
        
        increse_adult_element = self.find_elements(By.CLASS_NAME,"b9def0936d")

        for _ in range(count-1): # _ mean we didnt need of loop varaible
            increse_adult_element[2].click()
    
    def click_search(self):
        search_btn = self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        search_btn.click()
    
    def apply_filteration(self):
        filteration =  BookingFilteration(driver=self)
        filteration.apply_star_rating(4)
        filteration.sort_price_lowest_first()
    
    def report_results(self):
        hotel_boxes = self.find_element(By.ID,'search_results_table')
        
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names = ['Hotel Name','Hotel Price','Hotel Score']
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
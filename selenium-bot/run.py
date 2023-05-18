from booking.booking import Booking
import time

# inst = Booking()  <-- you can also write this
# inst.land_first_page()

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place(input('Where do you want to go ?'))
        bot.select_Date(check_in=input('What is checkIn date ?'),check_out=input('What is checkOut date ?'))
        bot.select_adults(int(input('How many people ?')))
        bot.click_search()
        bot.apply_filteration()
        bot.refresh() # for bot to grab data properly
        bot.report_results()

        time.sleep(30)

except Exception as e:
    print('Error',e)
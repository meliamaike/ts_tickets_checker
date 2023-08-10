import os
import time
import schedule
from selenium import webdriver
from bs4 import BeautifulSoup
import pywhatkit as kit
import webbrowser

url = "https://www.allaccess.com.ar/event/taylor-swift-the-eras-tour"
#url = "https://www.allaccess.com.ar/event/the-weeknd"


def open_new_tab(url):
    webbrowser.open_new_tab(url)

def check_ticket_availability():

    # Create ChromeOptions instance
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")

    agotado_div = soup.find("div", class_="coming_soon_picker")
    buy_btn = soup.find("button", id = "buyButton")

    if agotado_div:
        print("AGOTADO")
        return False  
    elif buy_btn:
        print("HAY ENTRADAS!")
        return True
    else:
        print("HAY ENTRADAS!")
        return True 


def send_whatsapp_message(message, recipient_phone_numbers):
    for phone_number in recipient_phone_numbers:
        kit.sendwhatmsg_instantly(phone_number, message, 15, True, 4)


def main():

    recipient_phone_numbers = [
        'PHONE_NUMBER_1',
        'PHONE_NUMBER_2',
        'ETC'
    ]

    while True:
        tickets_available = check_ticket_availability()
        if tickets_available:
            send_whatsapp_message(
                "HAY TICKETS PARA TAYLOR SWIFT!!!!!--> https://www.allaccess.com.ar/event/taylor-swift-the-eras-tour",
                recipient_phone_numbers)
            open_new_tab(url)
            time.sleep(3)  # Give some time for the page to load
            

            break

        time.sleep(5)
        

if __name__ == "__main__":
    main()



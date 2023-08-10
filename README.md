# TAYLOR SWIFT TICKET CHECKER 

This Python script monitors the ticket availability for the TAYLOR SWIFT | The Eras Tour in Argentina on the AllAccess website. 
It uses web scraping with Selenium and Beautiful Soup to determine whether tickets are available for purchase.

## Requirements

Install all the necessary packages.

    pip install -r requirements.txt

## Usage

1. Clone or download this repository to your local machine.

2. Install the required libraries mentioned in the 'Requirements' section using the provided pip commands.

3. Add the recipient phone numbers to the `recipient_phone_numbers` list within the `main` function.

4. Run the script using the following command:

   ```
   python ts_ticket_checker.py 
   ```

5. The script will continuously check for ticket availability. Once tickets become available, it will send a WhatsApp message to the specified phone numbers using PyWhatKit.

## Notes

- The script uses Chrome in headless mode to perform web scraping. Ensure you have the Chrome browser installed.
- This script is provided as-is and may require adjustments depending on changes to the website's structure.







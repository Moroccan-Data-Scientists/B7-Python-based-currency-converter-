import pandas as pd
import requests
from datetime import timedelta, date
from bs4 import BeautifulSoup
import streamlit as st

# TODO: Create a function to scrape the current currency rate
def rate_parser(input_curr, output_curr):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={input_curr}&To={output_curr}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')

    result_element = soup.find("p", class_="result__BigRate-sc-1bsijpp-1 dPdXSB")

    if result_element:
        currency_text = result_element.get_text().replace(',', '')  # Remove comma
        rate = float(currency_text.split()[0])
        return rate
    else:
        print(f"Element not found for {input_curr} to {output_curr}.")
        return None

# TODO: Create a function to convert an amount from currency to currency in real time
def convert(base, dest, amount):
    rate = rate_parser(base, dest)
    new_amount = rate * amount
    return new_amount

# TODO: Create a list of all supported currencies
currencies = ["USD", "EUR", "CAD", "MAD", "GBP", "AUD", "JPY"]
# this is just a test list
# TODO: Expand the list as needed

# Prompt user to enter an amount
amount = float(input("Amount: "))

# Prompt user to select base currency
print("From currency:")
base = input(f"Choose from {currencies}: ")

# Validate user input
while base not in currencies:
    print("Invalid currency entered. Please choose from the supported currencies.")
    base = input(f"Choose from {currencies}: ")

# Prompt user to select destination currency
print("To currency:")
dest = input(f"Choose from {currencies}: ")

# Validate user input
while dest not in currencies:
    print("Invalid currency entered. Please choose from the supported currencies.")
    dest = input(f"Choose from {currencies}: ")

# Calculate and display the result
current_rate = rate_parser(base, dest)
output = convert(base, dest, amount)

print("Success")
print(f"From currency: {base}")
print(f"To currency: {dest}")
print(f"Current exchange rate between {base} and {dest}: 1 {base} = {current_rate} {dest}")
print(f"Converted amount: {amount} {base} = {output} {dest}")

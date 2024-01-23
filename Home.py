
import pandas as pd
import requests
from datetime import timedelta, date
from bs4 import BeautifulSoup
import streamlit as st




#TODO:Create a function to scrape the current currency rate
    
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
    
#TODO:Create a function to convert an amount from currency to currency in real time
    
def convert(base,dest,amount):
    rate = rate_parser(base,dest)
    new_amount = rate * amount
    return new_amount 


#TODO:Create a list of all supported currencies

currencies = ["USD","EUR","CAD","MAD","GBP","AUD","JPY"]
#this is just a test lit
#TODO:Expend the list as needed

#TODO:Create the UI using streamlit


st.write("# Python based currency converter")

st.sidebar.write("### Currency converter:")


base = st.sidebar.selectbox("Enter a base currency:",currencies)

dest = st.sidebar.selectbox("Enter a destination currency:",currencies)

amount = st.sidebar.number_input("Enter an amount")

input = st.sidebar.button("Convert")



if input:
    current_rate = rate_parser(base,dest)
    output = convert(base,dest,amount)
    st.success("Success")
    st.write(f"## Current exchange rate between {base} and {dest} ")
    st.write(f"#### 1 {base} = ")
    st.write(f" ## :red[{current_rate}] {dest}")

    st.write("## Converted amount:")
    st.write(f" ### {amount} {base} = :red[{output}] {dest}")

    


    



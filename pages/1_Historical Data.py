import pandas as pd
import requests
from datetime import timedelta, date
from bs4 import BeautifulSoup
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

#TODO:Create a function to return a list of each day between two dates

def daterange(start_date, end_date):
    list = []
    for n in range(int ((end_date - start_date).days)):
        list.append(start_date + timedelta(n))
    return list



#TODO:Create a function that scrapes historical data nb(all apis didn't work well)

def historical_data(start_date,end_date,base,dest):
    df = pd.DataFrame()
    times = daterange(start_date, end_date)
    for single_date in times:
        dfs = pd.read_html(f'https://www.xe.com/currencytables/?from={base}&date={single_date.strftime("%Y-%m-%d")}')[0]
        dfs['Date'] = single_date.strftime("%Y-%m-%d")
        df = pd.concat([df, dfs], ignore_index=True)


    df_curr=df.loc[df['Currency']==dest]

    df_curr = df_curr.reset_index(drop=True)
    df_curr.set_index('Date',inplace = True)
    return df_curr


#TODO:Create a list of all supported currencies

currencies = ["USD","EUR","CAD","MAD","GBP","AUD","JPY"]
#this is just a test lit
#TODO:Expend the list as needed

#TODO:Create the UI using streamlit

st.write("# Historical Data:")
st.warning("This is originally a scraping webapp so choosing a large duration might cause substancial running time")
st.warning("Recommanded max duration : 1 Month")

base = st.sidebar.selectbox("Enter a base currency:",currencies)

dest = st.sidebar.selectbox("Enter a destination currency:",currencies)

start = st.sidebar.date_input("Enter start date:")

finish = st.sidebar.date_input("Enter finish date:")

input = st.sidebar.button("Confirm")

if input:
    if start == finish:
        st.error("Error: cannot process same date")
    with st.spinner('Wait for it...'):
        data = historical_data(start,finish,base,dest)
    st.success('Done!')
    st.table(data)
    st.write("## Plotting")
    
    st.write("### Static plot:")
    fig, ax = plt.subplots()
    ax.plot(data[f"{base} per unit"])
    ax.set_title(f'{base} to {dest} over Time')
    ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
    st.pyplot(fig)
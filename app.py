import streamlit as st
import sqlite3
import pandas as pd
#import matplotlib.pyplot as plt
#from wordcloud import WordCloud

####- Database Config
conn = sqlite3.connect('Jwell_shop.db')
cur = conn.cursor()
#-------

###### Database Operation Query----
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS loandata(pan)')


######### MAIN Function ########
def main():
    
    #sidebar menu with menu list
    menu=["Home","New Gold Loan","search Loan customer","Advance Repayment",'Analysis Graph']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.title("Welcome To Jwellary")
    

    elif choice == "New Gold Loan":
        st.subheader("New Gold loan Customer form")
        #create_table()
        #cus_pan = st.text_input("Pan Number")
        cus_pan=st.file_uploader("Pan Card")
        #cus_Adhar = st.text_input("AdharCard Number")
        cus_adhar = st.file_uploader("adhar Card")
        cus_name = st.text_input("Customer Name")
        cus_mobile = st.text_input("Mobile Number",max_chars=int(10),key=int)
        product = st.radio("Loan for",("Gold","Silver"))
        Loan_date = st.date_input("Date")
        if st.button("Add"):
            pass



if __name__=='__main__':
    main()
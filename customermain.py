#for admin of food website
"""https://mockupfree.co/get/18708"""
# Importing pakages
import streamlit as st
import mysql.connector

from database import addempdelivery
from create import createorder,createordeinmain
#from delete import deletemns,deleteemp
#from read import reademployee, readlowmns, readmns, readallemp,readpriv,readfoodord,readdeli
#from update import updateemp,updateord,updatemns

mydb = mysql.connector.connect(
     host="localhost",
     user="foodCustomer",
     password="password")
c = mydb.cursor()

def main2():
    #st.title("Gollas Food")
    mainmenu=['Place Order']
    mainchoice=st.sidebar.selectbox('Choose Desired Domain',mainmenu)
    if mainchoice=='Place Order':
       st.subheader('Please Choose items for the order')
       createordeinmain()
    #elif mainchoice=='Delete Account':
    #   st.subheader('Delete Account')     
    else:
        st.subheader("About tasks")

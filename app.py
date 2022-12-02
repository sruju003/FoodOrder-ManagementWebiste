#for admin of food website
"""https://mockupfree.co/get/18708"""
# Importing pakages
import streamlit as st
import mysql.connector

from create import createemployee
from delete import deletemns,deleteemp
from read import reademployee, readlowmns, readmns, readallemp,readpriv,readdeli,readfoodord,readratingemp,privemployee,readproc,readtrig,readnumord,viewtimbas
from update import updateemp,updateord,updatemns
from database import final
mydb = mysql.connector.connect(
     host="localhost",
     user="foodAdmin",
     password="password")
c = mydb.cursor()
#c.execute("CREATE DATABASE ebike")
#"""def main():
#    st.title("Gollas Food")
#    menu = ["Add", "View", "Edit", "Remove"]
#    choice = st.sidebar.selectbox("Menu", menu)"""



def main1():
    #st.title("Gollas Food")
    mainmenu=['Manage Employee','Manage Supply and Food','Manage Order and Delivery']
    mainchoice=st.sidebar.selectbox('Choose Desired Domain',mainmenu)
    if mainchoice=='Manage Employee':
        menuemp = ["View all Employee","View Rating Patterns","Employee Details","Add new employee","Edit Employee Details","Private Details","Need to update","Delete Employee"]
        choice = st.selectbox("Employee Info", menuemp)
        if choice == "View all Employee":
            st.subheader("View Employees")
            reademployee()
        elif choice=="View Rating Patterns":
            st.subheader("View rating aggregation")
            readratingemp()
        elif choice=="Need to update":
            st.subheader("Employee must update Private Details")
            privemployee()
        elif choice == "Employee Details":
            st.subheader("View Employees Details")
            readallemp()
        elif choice == "Add new employee":
            st.subheader("Add new employee")
            createemployee()
        elif choice == "Private Details":
            st.subheader("View Private Details")
            readpriv()
        elif choice == "Edit Employee Details":
            st.subheader("Update Values")
            updateemp()
        elif choice=="Delete Employee":
            st.subheader("Delete Employee details")
            deleteemp()
        else:
            st.subheader("About tasks")

    elif mainchoice=='Manage Supply and Food':
        menufood = ["Supply and Menu", "Reorder Stock info","Update Stock Info","Delete Item from Menu"]
        choice = st.selectbox("Food and supply Info", menufood)
        if choice == "Supply and Menu":
            st.subheader("View supply and menu")
            readmns()  
        elif choice == "Reorder Stock info":
            st.subheader("Items to be reordered")
            readlowmns()
        elif choice=="Update Stock Info":
            st.subheader("Update Stock Information")
            updatemns()
        elif choice=="Delete Item from Menu":
            st.subheader("Delete EItem from Menu")
            deletemns()
        else:
            st.subheader("About tasks")

    elif mainchoice=='Manage Order and Delivery':
        menuord = ["View Orders","View Delivery Details","View Earnings","Order between 12:00pm to 9:00pm > 4","View orders per customer"]
        choice = st.selectbox("Order and Delivery Information", menuord)
        if choice == "View Orders":
            st.subheader("View Order Details")
            readfoodord()  
        elif choice == "View Delivery Details":
            st.subheader("View Delivery Details")
            readdeli()
        elif choice=="View Earnings":
            st.subheader("View Earnings")
            readproc()
        elif choice=="Order between 12:00pm to 9:00pm > 4":
            st.subheader("View customer who ordered more than 4 times in given time")
            viewtimbas()
        elif choice=="View orders per customer":
            st.subheader("View orders per customer")
            readnumord()

        #elif choice=="Number of Orders":
        #    st.subheader("View Number of orders placed")
        #    readtrig()
        #elif choice=='Update Orders':
        #    st.subheader("Update Order Details")
        #    updateord()
            
        else:
            st.subheader("About tasks")


#if __name__ == '__main__':
#    main()

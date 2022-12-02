# for admins viewing 
import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data_emp , view_available_mns, view_lesser_mns, viewemp , viewempprv , viewdel,vieword,viewratingemp,viewnotpriv,viewproc,viewtrig,viewnumords,final

def reademployee():
    result = view_all_data_emp()
    # st.write(result)
    df = pd.DataFrame(result, columns=['EmpID', 'EmpName', 'Rating', 'Supervision','AadhaarID','PanNumber','Email','DL'])
    with st.expander("View all Employees"):
        st.dataframe(df)
def readmns():
    result = view_available_mns()
    # st.write(result)
    df = pd.DataFrame(result, columns=['ItemID', 'ItemName', 'ItemQnty', 'FoodAvailability','Price'])
    with st.expander("View all Menus and Supply"):
        st.dataframe(df)
def readpriv():
    result= viewempprv()
    df = pd.DataFrame(result, columns=['EmpID','AadhaarID','PanNumber','Email','DL'])
    with st.expander("View all Private Details"):
        st.dataframe(df)
def readfoodord():
    result= vieword()
    df = pd.DataFrame(result, columns=['CustomerID','OrderID','DateOfOrder','TimeOfOrder','Amount','PaymentMethod'])
    with st.expander("View all Order Details"):
        st.dataframe(df)
def readdeli():
    result= viewdel()
    df = pd.DataFrame(result, columns=['DeliveryID','Destination','DateOfOrd','DeliveryDoneBy'])
    with st.expander("View all Delivery Deatails"):
        st.dataframe(df)
def readallemp():
    result= viewemp()
    df = pd.DataFrame(result, columns=['EmpID','Employee Name','Rating','Supervision'])
    with st.expander("View Employee Details"):
        st.dataframe(df)
def readlowmns():
    result = view_lesser_mns()
    # st.write(result)
    df = pd.DataFrame(result, columns=['ItemName','ItemQnty','Status'])
    with st.expander("View Items running low and need to be ordered"):
        st.dataframe(df)

def readratingemp():
    result=viewratingemp()
    df=pd.DataFrame(result,columns=['Rating','NumberOfEmployees'])
    with st.expander("View rating history of employees"):
        st.dataframe(df)

def readtrig():
    result=viewtrig()
    df=pd.DataFrame(result,columns=['No. of orders placed'])
    with st.expander("View number of orders placed"):
        st.dataframe(df)

def readproc():
    result=viewproc()
    df=pd.DataFrame(result,columns=['Total earnings'])
    with st.expander("View Earnings"):
        st.dataframe(df)

def readnumord():
    result=viewnumords()
    df=pd.DataFrame(result,columns=['CustomerID','Numberoforders'])
    with st.expander('View orders from time 12pm to 9pm'):
        st.dataframe(df)

def viewtimbas():
    result=final()
    df=pd.DataFrame(result,columns=['CustomerID','Regularity'])
    with st.expander("View all order details for more than 4 time between 12 to 9"):
        st.dataframe(df)

def privemployee():
    result=viewnotpriv()
    df = pd.DataFrame(result, columns=['EmpID','Employee Name','Rating','Supervision'])
    with st.expander("View Employee Details"):
        st.dataframe(df)

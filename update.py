import datetime

import pandas as pd
import streamlit as st
from database import get_emp, editempdata , get_ord, editorddata,get_mns
from database import view_all_data_emp ,view_empNames , vieword , viewordID , viewallmns, mnsname ,editmnsdata


def updateemp():
    result = view_all_data_emp()
    # st.write(result)
    df = pd.DataFrame(result, columns=['EmpID', 'EmpName', 'Rating', 'Supervision','AadhaarID','PanNumber','Email','DL'])
    with st.expander("Current Employees"):
        st.dataframe(df)
    list_of_emp = [i[0] for i in view_empNames()]
    selected_emp = st.selectbox("EmpID to Edit", list_of_emp)
    selected_result = get_emp(selected_emp)
    # st.write(selected_result)
    if selected_result:
        empID = selected_result[0][0]
        Empname = selected_result[0][1]
        ratingemp = selected_result[0][2]
        supervisionemp = selected_result[0][3]
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            newempID = st.text_input("ID:", empID)
            newEmpname = st.text_input("Name:", Empname)
        with col2:
            newratingemp = st.text_input("Rating", ratingemp)
            newsupervisionemp = st.text_input("Supervision:", supervisionemp)
        if st.button("Update Employee"):
            editempdata(newempID,newEmpname,newratingemp,newsupervisionemp,empID,Empname,ratingemp,supervisionemp)
            st.success("Successfully updated:: {} to ::{}".format(Empname, newEmpname))

    result2 = view_all_data_emp()
    df2 = pd.DataFrame(result2, columns=['EmpID', 'EmpName', 'Rating', 'Supervision','AadhaarID','PanNumber','Email','DL'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#-----------------------------------------------------------------------------------------------------------------

def updateord():
    result = vieword()
    # st.write(result)
    df = pd.DataFrame(result, columns=['CustomerID','OrderID','FoodID','FoodStatus','Amount','FoodPay','TimeOfOrder'])
    with st.expander("Current Orders"):
        st.dataframe(df)
    list_of_orders = [i[0] for i in viewordID()]
    selected_ord = st.selectbox("Order to Edit", list_of_orders)
    selected_result = get_ord(selected_ord)
    # st.write(selected_result)
    if selected_result:
        CustID = selected_result[0][0]
        OrdID = selected_result[0][1]
        FoodD = selected_result[0][2]
        FoodStatus = selected_result[0][3]
        TotalAmt= selected_result[0][4]
        Foodpay = selected_result[0][5]
        TofFood= selected_result[0][6]
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            newCustID = st.text_input(" Customer ID:", CustID)
            newOrdID = st.text_input(" Order ID:", OrdID)
            newFoodD = st.text_input(" Date of Order:", FoodD)
        with col2:
            newFoodStatus = st.text_input(" Food Status:", FoodStatus)
            newTotalAmt = st.text_input("Total Amount:", TotalAmt)
            newFoodpay = st.text_input("Payment Method :", Foodpay)
        if st.button("Update Orders "):
            editorddata(newCustID,newOrdID,newFoodD,newFoodStatus,newTotalAmt,newFoodpay,CustID,OrdID,FoodD,FoodStatus,TotalAmt,Foodpay)
            st.success("Successfully updated:: {} to ::{}".format(OrdID, newOrdID))

    result2 = vieword()
    df2 = pd.DataFrame(result2, columns=['CustomerID','OrderID','FoodID','FoodStatus','Amount','FoodPay','TimeOfOrder'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#----------------------------------------------------------------------------------------------------------------

def updatemns():
    result = viewallmns()
    # st.write(result)
    df = pd.DataFrame(result, columns=['ItemID', 'ItemName', 'ItemQnty', 'FoodAvailability','Price'])
    with st.expander("Current Menu and Supply"):
        st.dataframe(df)
    list_of_mns = [i[0] for i in mnsname()]
    selected_mns = st.selectbox("Order to Edit", list_of_mns)
    selected_result = get_mns(selected_mns)
    # st.write(selected_result)
    if selected_result:
        ItemID = selected_result[0][0]
        ItemName = selected_result[0][1]
        ItemQnty = selected_result[0][2]
        FoodAvailibility = selected_result[0][3]
        Price = selected_result[0][4]
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            newItemID = st.text_input(" Item ID:", ItemID)
            newItemName = st.text_input(" Item Name:", ItemName)
            newItemQnty = st.text_input(" Item Quantity:", ItemQnty)
        with col2:
            newFoodAvailibility = st.text_input(" Food Availibility:", FoodAvailibility)
            newPrice = st.text_input("Price/item:", Price)
        if st.button("Update Orders "):
            editmnsdata(newItemID,newItemName,newItemQnty,newFoodAvailibility,newPrice,ItemID,ItemName,ItemQnty,FoodAvailibility,Price)
            st.success("Successfully updated:: {} to ::{}".format(ItemName, newItemName))

    result2 = viewallmns()
    df2 = pd.DataFrame(result2, columns=['ItemID', 'ItemName', 'ItemQnty', 'FoodAvailability','Price'])
    with st.expander("Updated data"):
        st.dataframe(df2)
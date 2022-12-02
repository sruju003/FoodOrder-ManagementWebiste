import pandas as pd
import streamlit as st

from database import view_all_data_emp, view_empNames, mnsname , viewallmns
from database import delete_dataemp, delete_datamns
#from database import view_all_data, view_only_dealer_names, delete_data


def deleteemp():
    result = view_all_data_emp()
    df = pd.DataFrame(result, columns=['EmpID', 'EmpName', 'Rating', 'Supervision','AadhaarID','PanNumber','Email','DL'])
    with st.expander("Current data"):
        st.dataframe(df)
    #list_of_emp = [i[0] for i in view_empNames()]
    list_of_emp = [i[0] for i in view_empNames()]
    selected_emp = st.selectbox("Employee to Delete", list_of_emp)
    st.warning("Do you want to delete ::{}".format(selected_emp))
    if st.button("Delete Employee"):
        delete_dataemp(selected_emp)
        st.success("Employee has been deleted successfully")
    new_result = view_all_data_emp()
    df2 = pd.DataFrame(new_result, columns=['EmpID', 'EmpName', 'Rating', 'Supervision','AadhaarID','PanNumber','Email','DL'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def deletemns():
    result = viewallmns()
    df = pd.DataFrame(result, columns=['ItemID', 'ItemName', 'ItemQnty', 'FoodAvailability','Price'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_mns = [i[0] for i in mnsname()]
    selected_mns = st.selectbox("Task to Delete", list_of_mns)
    st.warning("Do you want to delete ::{}".format(selected_mns))
    if st.button("Delete Item from Menu and Supply"):
        delete_datamns(selected_mns)
        st.success("Item has been deleted successfully")
    new_result = viewallmns()
    df2 = pd.DataFrame(new_result, columns=['ItemID', 'ItemName', 'ItemQnty', 'FoodAvailability','Price'])
    with st.expander("Updated data"):
        st.dataframe(df2)
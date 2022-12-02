import streamlit as st
from database import viewordnum,mnsname,quantityfood,pricefood,addordermain,addintocustord,addempdata,addintomainord,addempdelivery


def createordeinmain():
    col1,col2=st.columns(2)
    st.subheader('Welcome C1, are we ready to order today?')
    if st.button('Proceed',key=1000000):
        optionsofselect=['Gpay','COD']

        with col1:
            paymentmethod=st.selectbox('choose payment',optionsofselect)
            if paymentmethod:
                addordermain(paymentmethod)
        with col2:
            st.text('')
            st.text('')
            if st.button("Confirm placement of order"):
                st.success("Successfully added Order")       
    st.subheader('Choose items')            
    createorder()





def createorderold():
    col1, col2 = st.columns(2)
    position=0
    count=0
    #a=viewordnum()
    #current=a[position]
    with col1:
        list_of_mns = [i[0] for i in mnsname()]
        selected_mns = st.selectbox("Select Item", list_of_mns,key=count) # selecting menu item
        selected_result = quantityfood(selected_mns)
        minimufoo=selected_result[0][0]
        i=st.number_input('Quantity of food',min_value=0,max_value=minimufoo,key=count+100) #quantity of food
    with col2:
        price=pricefood(selected_mns)
        fprice=price[0][0]
        finalvalitem=i*fprice
            #st.text('Price of items :')
            #st.text(finalvalitem)
        count+=1
        finalval=finalvalitem+finalval
    #dealer_street = st.text_input("Street Name:")
    if st.button("Add Dealer"):
        add_orderdata(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
        st.success("Successfully added Dealer: {}".format(dealer_name))


def createorder():
    l=[0,1,2]
    finalval=0
    col1,col2=st.columns(2,gap='large')
    with col1:
            count=0
            list_of_mns = [i[0] for i in mnsname()]
            selected_mns = st.selectbox("Select Item", list_of_mns,key=count) # item name
            selected_result = quantityfood(selected_mns)
            minimufoo=selected_result[0][0]
            i=st.number_input('Quantity of food',min_value=0,max_value=minimufoo,key=count+100) # quantity of food
            price=pricefood(selected_mns)
            fprice=price[0][0]
            finalvalitem=i*fprice
            #st.text('Price of items :')
            #st.text(finalvalitem)
            count+=1
            finalval=finalvalitem+finalval
    with col2:
        st.subheader('Your final amount for the bill is:')
        st.header(finalval)
        if st.button(label='Confirm Order!'):
            addempdelivery()
            addintocustord(selected_mns,i)
            addintomainord(finalval)
            st.success('Successfully placed order!!')
            

def createemployee():
    col1, col2 = st.columns(2)
    with col1:
        employeeid=st.text_input('Enter Employee ID')
        employeename=st.text_input("Enter Employee name")
    with col2:
        rating=st.number_input('Enter employee rating',min_value=0,max_value=5)
        super=st.text_input('Enter supervision of employee')
    if st.button("Add Employee"):
        addempdata(employeeid,employeename,rating,super)
        st.success("Successfully added Employee: {}".format(employeename))

    

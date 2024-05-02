import pandas as pd
import numpy as np
import streamlit as st
from streamlit import session_state as ss



def main():
    # main page
    st.title('Hotel Cancellation Prediction')
    welcome = '''
              <font color='#BDD5EA' size=5>Welcome,
              <p> This app has been created to help people in the hospitality industry view the risk of a hotel booking being cancelled based on the
              guests information and booking details. Please input the necessary information on the sidebar to the left and press
              the <font color='red'>Run</font> button to generate the bookings cancellation probability.</font>
              <br>
              <br>
              <center><font color='#FF3366' size=12> Probability of Cancellation </font></center>
              '''
    st.markdown(welcome, unsafe_allow_html=True)
    # sidebar
    st.sidebar.header('Enter Booking Information')
    hotel_type = {'City Hotel': 1,
                    'Resort Hotel': 0}
    st.sidebar.selectbox('Hotel Type', options=hotel_type.keys(), key='hotel')
    st.sidebar.number_input('Number of Adults', min_value=1,max_value=55,step=1, key='adults')
    is_repeated_guest = {'Yes': 1,
                    'No': 0}
    st.sidebar.selectbox('Repeated Guest?', options=is_repeated_guest.keys(), key='is_repeated_guest')
    st.sidebar.number_input('Number of previous bookings that were cancelled by the customer', min_value=0, max_value=26,step=1,key='previous_cancellations')
    st.sidebar.number_input('Number of previous bookings not cancelled by the customer', min_value=0, max_value=72,step=1, key='previous_bookings_not_canceled')
    reserved_room_type = {'C': 0, 'A': 1, 'D': 2, 'E': 3, 'G': 4, 'F': 5, 'I': 6, 'B': 7, 'H': 8}
    st.sidebar.selectbox('Reserved Room Type', options=reserved_room_type.keys(), key='reserved_room_type')
    assigned_room_type = {'C': 0, 'A': 1, 'D': 2, 'E': 3, 'G': 4, 'F': 5, 'I': 6, 'B': 7, 'H': 8, 'P': 9, 'L': 10}
    st.sidebar.selectbox('Assigned Room Type', options=assigned_room_type.keys(), key='assigned_room_type')
    st.sidebar.number_input('Number of booking changes', min_value=0,max_value=18,step=1, key='booking_changes')
    st.sidebar.number_input('Days in Waiting List', min_value=0,max_value=391,step=1, key='days_in_waiting_list')
    st.sidebar.number_input('ADR', min_value=0, key='adr')
    st.sidebar.number_input('Required car parking spaces', min_value=0,max_value=8,step=1, key='required_car_parking_spaces')
    st.sidebar.number_input('Number of Special Request',
                            min_value=0,
                            max_value=5,
                            step=1,
                            key='total_of_special_requests')
    st.sidebar.number_input('Booking Lead Time', min_value=0, key='lead_time')
    st.sidebar.number_input('Total Number of Stays', min_value=0,max_value=69,step=1, key='total_stays')
    st.sidebar.number_input('Number of Kids', min_value=1,max_value=10,step=1, key='kids')
    meal_options = ['BB', 'FB', 'HB', 'SC']
    meal_type = st.sidebar.selectbox('Meal Type', options=meal_options)
    meal_df = pd.DataFrame(columns=meal_options)
    for option in meal_options:
        if option == meal_type:
            meal_df[option] = [1]
        else:
            meal_df[option] = [0]
    deposit = ['No Deposit', 'Refundable', 'Non Refund']
    deposit_type = st.sidebar.selectbox('Deposit Type', options=deposit)
    deposit_type_df = pd.DataFrame(columns=meal_options)
    for option in deposit:
        if option == deposit:
            deposit_type_df[option] = [1]
        else:
            deposit_type_df[option] = [0]
    customer = ['Transient', 'Contract', 'Transient-Party','Group']
    customer_type = st.sidebar.selectbox('Deposit Type', options=customer)
    customer_type_df = pd.DataFrame(columns=meal_options)
    for option in customer:
        if option == customer:
            customer_type_df[option] = [1]
        else:
            customer_type_df[option] = [0]
    st.sidebar.number_input('Reservation Month',min_value=1,max_value=12,step=1,key='reservation_month')
    st.sidebar.selectbox('Reservation Year', options=[2014,2015,2016,2017], key='reservation_year')
    st.sidebar.number_input('Total Number of Guests',min_value=1,max_value=4,step=1,key='total_guests')
    market_options = ['Direct', 'Corporate', 'Online TA', 'Offline TA/TO','Complementary','Groups','Aviation']
    market_type = st.sidebar.selectbox('Market', options=market_options)

    market_df = pd.DataFrame(columns=market_options)
    for option in market_options:
        if option == market_type:
            market_df[option] = [1]
        else:
            market_df[option] = [0]
    distribution_options = ['Dist Direct', 'Dist Corporate', 'Dist TA/TO','GDS']
    distribution_type = st.sidebar.selectbox('Distribution Channel', options=distribution_options)

    distribution_df = pd.DataFrame(columns=distribution_options)
    for option in distribution_options:
        if option == distribution_type:
            distribution_df[option] = [1]
        else:
            distribution_df[option] = [0]

 # calculate probability
    st.sidebar.button('Run', key='run')
    if ss.run:
        # create array of input data
        input_data = np.array([
    hotel_type[st.session_state.hotel],
    st.session_state.adults,
    is_repeated_guest[st.session_state.is_repeated_guest],
    st.session_state.previous_cancellations,
    st.session_state.previous_bookings_not_canceled,
    reserved_room_type[st.session_state.reserved_room_type],
    assigned_room_type[st.session_state.assigned_room_type],
    st.session_state.booking_changes,
    st.session_state.days_in_waiting_list,
    st.session_state.adr,
    st.session_state.required_car_parking_spaces,
    st.session_state.total_of_special_requests,
    st.session_state.lead_time,
    st.session_state.total_stays,
    st.session_state.kids,
    meal_df['BB'][0],  # Value for 'BB' meal type
    meal_df['FB'][0],  # Value for 'FB' meal type
    meal_df['HB'][0],  # Value for 'HB' meal type
    meal_df['SC'][0],  # Value for 'SC' meal type
    deposit_type_df['No Deposit'][0],  # Value for 'No Deposit' deposit type
    deposit_type_df['Refundable'][0],  # Value for 'Refundable' deposit type
    deposit_type_df['Non Refund'][0],  # Value for 'Non Refund' deposit type
    customer_type_df['Transient'][0],  # Value for 'Transient' customer type
    customer_type_df['Contract'][0],  # Value for 'Contract' customer type
    customer_type_df['Transient-Party'][0],  # Value for 'Transient-Party' customer type
    customer_type_df['Group'][0],  # Value for 'Group' customer type
    st.session_state.reservation_month,
    st.session_state.reservation_year,
    st.session_state.total_guests,
    market_df['Direct'][0],  # Value for 'Direct' market type
    market_df['Corporate'][0],  # Value for 'Corporate' market type
    market_df['Online TA'][0],  # Value for 'Online TA' market type
    market_df['Offline TA/TO'][0],  # Value for 'Offline TA/TO' market type
    market_df['Complementary'][0],  # Value for 'Complementary' market type
    market_df['Groups'][0],  # Value for 'Groups' market type
    market_df['Aviation'][0],  # Value for 'Aviation' market type
    distribution_df['Dist Direct'][0],  # Value for 'Direct' distribution channel
    distribution_df['Dist Corporate'][0],  # Value for 'Corporate' distribution channel
    distribution_df['Dist TA/TO'][0],  # Value for 'TA/TO' distribution channel
    distribution_df['GDS'][0],  # Value for 'GDS' distribution channel
]).reshape(1, -1)
        
        data = pd.read_csv('Post-cleaning Data.csv', index_col=0)
        scaler = StandardScaler()
        scaler.fit(data)
        input_norm = scaler.transform(input_data)
        # load model
        model = load('Phase 4 Model.joblib')
        # make prediction
        result = model.predict_proba(input_norm)
        proba = np.round(result[0][1]*100,2)
        # display prediction
        if proba < 50:
            color = '#7ABD91'
        else:
            color = '#FF6962'
        st.markdown(f'''
        <center><font color={color} size=12> {proba}% </font></center>
        ''', unsafe_allow_html=True)
        if proba < 50:
            st.balloons()
        else:
            st.snow()



if __name__ == '__main__':
    main()




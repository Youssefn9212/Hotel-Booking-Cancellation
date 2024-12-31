
#"D:\youssef\Desktop\AUC\Spring 2024\ML\Projects\Phase 5\phase_5.py"

import pandas as pd
import numpy as np
import streamlit as st
from streamlit import session_state as ss
import pickle


def main(): 
    # main page
    st.title('Hotel Cancellation Prediction')
    welcome = '''
              <font color='#FFFFFF' size=5>Welcome,
              <p> This app has been created to help people in the hospitality industry view the risk of a hotel booking being cancelled based on the
              guests information and booking details. Please input the necessary information on the sidebar to the left and press
              the <font color='red'>Run</font> button to generate the bookings cancellation probability and information regarding the model used.</font>
              <br>
              <br>
              '''
    st.markdown(welcome, unsafe_allow_html=True)
    css = """

    [data-testid="stSidebar"] {

        background-color: rgb(0, 53, 128);

    }

"""
# Apply the custom CSS using the `write` function

    st.write("<style>{}</style>".format(css), unsafe_allow_html=True)
    

    # sidebar
    st.sidebar.header('Enter Booking Information')
    hotel= {'City Hotel': 1,
                    'Resort Hotel': 0}
    st.sidebar.selectbox('Hotel Type', options=hotel.keys(), key='hotel')
    st.sidebar.number_input('Arrival Date Year', min_value=2014,max_value=2017,step=1, key='arrival_date_year')
    st.sidebar.number_input('Arrival Date Month',min_value=1,max_value=12,step=1,key='arrival_date_month')
    st.sidebar.number_input('Number of Adults', min_value=1,max_value=55,step=1, key='adults')
    st.sidebar.number_input('Number of Children', min_value=0,key='children')
    st.sidebar.number_input('Number of Babies',min_value=0, key='babies')
    st.sidebar.number_input('Country',min_value=0,max_value=176,step=1,key='country')
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
    st.sidebar.number_input('Agent ID', min_value=0,max_value=394,step=1, key='agent')
    st.sidebar.number_input('Days in Waiting List', min_value=0,max_value=391,step=1, key='days_in_waiting_list')
    st.sidebar.number_input('ADR', min_value=0, key='adr')
    st.sidebar.number_input('Required car parking spaces', min_value=0,max_value=8,step=1, key='required_car_parking_spaces')
    st.sidebar.number_input('Number of Special Request',min_value=0,max_value=5,step=1,key='total_of_special_requests')
    st.sidebar.number_input('Booking Lead Time',  key='lead_time')
    st.sidebar.number_input('Total Number of Stays', min_value=0,max_value=69,step=1, key='total_stays')
    st.sidebar.number_input('Number of Kids', min_value=1,max_value=10,step=1, key='kids')
    meal_type = st.sidebar.subheader('Meal Type')
    if meal_type:
       meal_options = ['BB', 'FB', 'HB', 'SC']
       meal_type_selected = st.sidebar.selectbox('Select Customer Meal Type:', meal_options)
    else:
       meal_type_selected = []
    
    user_inputs1 = np.zeros((1, 4))
    if 'BB' in meal_type_selected:
        user_inputs1[:, 0] = 1
    if 'FB' in meal_type_selected:
        user_inputs1[:, 1] = 1
    if 'HB' in meal_type_selected:
        user_inputs1[:, 2] = 1
    if 'SC' in meal_type_selected:
        user_inputs1[:, 3] = 1
        
    market_type = st.sidebar.subheader('Customter Market')
    if market_type:
        market_type_options =  ['Direct', 'Corporate', 'Online TA', 'Offline TA/TO','Complementary','Groups','Aviation']
        market_type_selected = st.sidebar.selectbox('Select Customer Market:',
                                                             market_type_options)
    else:
        market_type_selected = []

    user_inputs5 = np.zeros((1, 7))
    if 'Direct' in market_type_selected:
        user_inputs5[:, 0] = 1
    if 'Corporate' in market_type_selected:
        user_inputs5[:, 1] = 1
    if 'Online TA' in market_type_selected:
        user_inputs5[:, 2] = 1
    if 'Offline TA/TO' in market_type_selected:
        user_inputs5[:, 3] = 1
    if 'Complementary' in market_type_selected:
        user_inputs5[:, 4] = 1
    if 'Groups' in market_type_selected:
        user_inputs5[:, 5] = 1
    if 'Aviation' in market_type_selected:
        user_inputs5[:, 6] = 1
    
    distribution_channel = st.sidebar.subheader('Distribution Channel')
    if distribution_channel:
        distribution_options = ['Dist Direct', 'Dist Corporate', 'Dist TA/TO','GDS']
        distribution_channel_selected = st.sidebar.selectbox('Select Distribution Channel:', distribution_options)
    else:
        distribution_channel_selected = []

    user_inputs2 = np.zeros((1, 4))
    if 'Dist Direct' in distribution_channel_selected:
        user_inputs2[:, 0] = 1
    if 'Dist Corporate' in distribution_channel_selected:
        user_inputs2[:, 1] = 1
    if 'CorporateDist TA/TO' in distribution_channel_selected:
        user_inputs2[:, 2] = 1
    if 'GDS' in distribution_channel_selected:
        user_inputs2[:, 3] = 1
        
    deposit_type = st.sidebar.subheader('Deposit Type')
    if deposit_type:
        deposit_type_options = ['No Deposit', 'Refundable', 'Non Refund']
        deposit_type_selected = st.sidebar.selectbox('Select Deposit Type:', deposit_type_options)
    else:
        deposit_type_selected = []

    user_inputs3 = np.zeros((1, 3))
    if 'No Deposit' in deposit_type_selected:
        user_inputs3[:, 0] = 1
    if 'Refundable' in deposit_type_selected:
        user_inputs3[:, 1] = 1
    if 'Non Refund' in deposit_type_selected:
        user_inputs3[:, 2] = 1
        
    customer_type = st.sidebar.subheader('Customer Type')
    if customer_type:
         customer_type_options = ['Transient', 'Contract', 'Transient-Party', 'Group']
         customer_type_selected = st.sidebar.selectbox('Select Customer Type:',
                                                              customer_type_options)
    else:
         customer_type_selected = []

    user_inputs4 = np.zeros((1, 4))
    if 'Transient' in customer_type_selected:
         user_inputs4[:, 0] = 1
    if 'Contract' in customer_type_selected:
         user_inputs4[:, 1] = 1
    if 'Transient-Party' in customer_type_selected:
         user_inputs4[:, 2] = 1
    if 'Group' in customer_type_selected:
         user_inputs4[:, 3] = 1
     
        
    st.sidebar.number_input('Reservation Year', min_value=2014,max_value=2017,step=1, key='reservation_year')
    st.sidebar.number_input('Reservation Month',min_value=1,max_value=12,step=1,key='reservation_month')
    st.sidebar.number_input('Total Number of Guests',min_value=1,max_value=4,step=1,key='total_guests')
   
    
    
    
    

 # calculate probability
    st.sidebar.button('Run', key='run')
    if ss.run:
        input_data = np.array([
            hotel[ss.hotel],
            ss.arrival_date_year,
            ss.arrival_date_month,
            ss.adults,
            ss.children,
            ss.babies,
            ss.country,
            is_repeated_guest[ss.is_repeated_guest],
            ss.previous_cancellations,
            ss.previous_bookings_not_canceled,
            reserved_room_type[ss.reserved_room_type],
            assigned_room_type[ss.assigned_room_type],
            ss.booking_changes,
            ss.agent,
            ss.days_in_waiting_list,
            ss.adr,
            ss.required_car_parking_spaces,
            ss.total_of_special_requests,
            ss.lead_time,
            ss.total_stays,
            ss.kids,
            # meal_type_selected
            user_inputs1[0][0],
            user_inputs1[0][1],
            user_inputs1[0][2],
            user_inputs1[0][3],
            #market_type_selected
            user_inputs5[0][0],
            user_inputs5[0][1],
            user_inputs5[0][2],
            user_inputs5[0][3],
            user_inputs5[0][4],
            user_inputs5[0][5],
            user_inputs5[0][6],
            # distribution_channel_selected
            user_inputs2[0][0],
            user_inputs2[0][1],
            user_inputs2[0][2],
            user_inputs2[0][3],
            # deposit_type_selected
            user_inputs3[0][0],
            user_inputs3[0][1],
            user_inputs3[0][2],
            # customer_type_selected
            user_inputs4[0][0],
            user_inputs4[0][1],
            user_inputs4[0][2],
            user_inputs4[0][3],
            ss.reservation_year,
            ss.reservation_month,
            ss.total_guests               
        ]).reshape(1, 46)
        
        model = pickle.load(open('D:/youssef/Desktop/AUC/Spring 2024/ML/Projects/Phase 5/Phase 4 Model.pkl', 'rb'))
        result = model.predict_proba(input_data)
        proba = np.round(result[0][1]*100 , 2)
        
        st.subheader('Model Probability Prediction')
        if proba < 50:
            color = '#008000'
        elif 50 <= proba < 80:
            color = '#FFFF00'
        else: 
            color = '#FF0000'

        st.markdown(f'''
                    <center><font color={color} size=7> {proba}% </font></center>
                    ''', unsafe_allow_html=True)
                    
        st.subheader('Model Information and HyperParameters')
        
        parameters = ''' 
                      <font color='#FFFFFF' size=12>
                      <p> The model used to predict the hotel cancellations is Random Forest with the following 
                      parameters:
                      
                      '''
        st.markdown(parameters, unsafe_allow_html=True)
    
        st.info('Min Sample Splits: 3')
        st.info('Min Sample Leafs: 2')
        st.info('Max Features: log2')
        st.info('Max Depth: 100')
        st.info('Bootstrap: False')

        
        st.subheader('Model Evaluation')

        # Load and display the image with a caption
        image_path = "D:/youssef/Desktop/AUC/Spring 2024/ML/Projects/Phase 5/Untitled.png"
        st.image(image_path, use_column_width=True, caption='Confusion Matrix')

        # Display training and test accuracy
        st.text('Training Accuracy: 0.996517027863777')
        st.text('Test Accuracy: 0.9377440845393982')
        
        # Display F1 score
        st.text('F1 Score: 0.921')
        
        ## Classification report data
        classification_data = {
            '': ['0', '1', 'accuracy', 'macro avg', 'weighted avg'],
            'precision': [0.93, 0.96, '', 0.94, 0.94],
            'recall': [0.97, 0.89, '', 0.93, 0.94],
            'f1-score': [0.95, 0.92, 0.94, 0.93, 0.94],
            'support': ['2568', '1785', '4353', '4353', '4353']
        }
        
        # Create a DataFrame from the classification report data
        classification_df = pd.DataFrame(classification_data)
        
        # Set the index to the empty column
        classification_df.set_index('', inplace=True)
        
        # Display the classification report as a table
        st.subheader('Classification Report')
        st.table(classification_df)
                


        
        
if __name__ == '__main__':
    main()
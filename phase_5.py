# -*- coding: utf-8 -*-
"""Phase 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Rh8d4OAud4v1EQXEN8-286QYrUnnKy0Q
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, recall_score, precision_score, confusion_matrix
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.feature_selection import SelectFromModel, SelectPercentile
from sklearn.metrics import f1_score, confusion_matrix

import pandas as pd
import numpy as np
from joblib import load, dump
import streamlit as st
from streamlit import session_state as ss
from sklearn.preprocessing import StandardScaler


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


  st.sidebar.header('Select Meal Type')
    meal_options = ['BB', 'FB', 'HB', 'SC']
    meal_type = st.sidebar.selectbox('Meal Type', options=meal_options)

    # Create DataFrame to store meal type selection
    meal_df = pd.DataFrame(columns=meal_options)
    for option in meal_options:
        if option == meal_type:
            meal_df[option] = [1]
        else:
            meal_df[option] = [0]

    st.write('Meal Type DataFrame:')
    st.write(meal_df)

    st.sidebar.number_input('Total Number of Guests', key='total_guests')


    # calculate probability
    st.sidebar.button('Run', key='run')
    if ss.run:
        # create array of input data
        input_data = np.array([
            deposit_type[ss.deposit_type],
            ss.lead_time,
            ss.adr,
            ss.total_of_special_requests,
            ss.previous_cancellations,
            market_segment[ss.market_segment],
            ss.agent,
            customer_type[ss.customer_type]
        ]).reshape(1,8)
        # pre-process input data
        data = pd.read_csv('cleaned_features.csv', index_col=0)
        scaler = StandardScaler()
        scaler.fit(data)
        input_norm = scaler.transform(input_data)
        # load model
        model = load('hotel_app_logistic_regression_model.joblib')
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

import streamlit as st
import pandas as pd

def main():
    st.sidebar.header('Select Meal Type')
    meal_options = ['BB', 'FB', 'HB', 'SC']
    meal_type = st.sidebar.selectbox('Meal Type', options=meal_options)

    # Create DataFrame to store meal type selection
    meal_df = pd.DataFrame(columns=meal_options)
    for option in meal_options:
        if option == meal_type:
            meal_df[option] = [1]
        else:
            meal_df[option] = [0]

    st.write('Meal Type DataFrame:')
    st.write(meal_df)

if __name__ == "__main__":
    main()

streamlit run app.py
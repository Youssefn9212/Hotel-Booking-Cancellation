




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


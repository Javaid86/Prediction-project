import streamlit as st
import numpy as np
# from joblib import load
import joblib

model = joblib.load('model.pkl')

# Define the Streamlit app
def main():
    # Set the title of the app
    st.title('Prediction App')

    # Add number input widgets for user to enter input values
    input1 = st.number_input('Enter input E:', value=0)
    input2 = st.number_input('Enter input I:', value=0)
    input3 = st.number_input('Enter input TON:', value=0)
    # Check if inputs are integers
    if not (isinstance(input1, int) and isinstance(input2, int)):
        st.error('Please enter integer values for input I and input TON.')
        return
    if st.button('Predict'):
        # Make prediction using the model
        prediction = model.predict(np.array([[input1, input2,input3]]))

    # Display the prediction

        st.write('Prediction:', prediction)
        st.write('SR:', 0)
        st.write('WLT:', 1)
        st.write('MRR:', 2)


if __name__ == "__main__":
    main()
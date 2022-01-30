# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 01:30:27 2022

@author: samra.afreen
"""
#CODE IN SPYDER
import numpy as np
import pickle      # used for loading the saved file
import streamlit as st #used for deployment

# Loading the saved model
loaded_model = pickle.load(open('C:/Users/samra.afreen/Anaconda3/Samra/trained_model.sav', 'rb'))


#Creating a function for prediction
def heart_disease_prediction(input_data):
# change input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if ( prediction[0] == 0):
        return 'The person does not have Heart disease'
    else:
        return 'The person have Heart disease'
    
    
def main():
    
    # Giving a title for web page
    st.title('Heart Disease Prediction Web App')
    
    # Getting the input data from user
    age = st.text_input('Age of a Person')
    sex = st.text_input('Gender')
    cp = st.text_input('Chest Pain type')
    trestbps = st.text_input('The person\'s resting blood pressure in mm/Hg')
    chol = st.text_input('Serum Cholesterol in mg/dl')
    fbs = st.text_input('The person\'s fasting blood sugar in mg/dl')
    restecg=st.text_input('resting electrocardiographic results')
    thalach=st.text_input('Maximum heart rate achieved')
    exang=st.text_input('Exercise Induced Angina')
    oldpeak=st.text_input('ST depression induced by exercise relative to rest')
    slope=st.text_input('ST segment shift relative to exercise-induced')
    ca=st.text_input('number of major vessels')
    thal=st.text_input('Thalassemia(blood disorder)')
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    
    if st.button('Heart Test Result'):
        diagnosis = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()
    
       # run in Anaconda prompt just after opening it
       # make sure streamlit is there
       # else pip install streamlit
       # streamlit run "C:\Users\samra.afreen\Anaconda3\Samra\Heart_Disease_Prediction_webApp.py"
       # web page willl open up and enter the values
    
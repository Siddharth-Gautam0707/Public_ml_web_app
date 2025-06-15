# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 21:06:04 2025

@author: sg474
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

#loading saved models sav file
diabetes_model = pickle.load(open('trained_model_new.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

#sidebar fir navigate

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System",
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'], #from bootstrap check those name
                           
                           default_index=0)
    

#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    #getting the input data from user 
    #columns for input fields 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies') 
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin value')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button 
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]])
        
        if(diab_prediction[0] == 1):
            diab_diagnosis = "The Person is Diabetic"
        else:
            diab_diagnosis = "The Person is not Diabetic"
            
    st.success(diab_diagnosis)


if(selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    #getting the input data from user 
    #columns for input fields 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age') 
    
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain Types')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    
    with col2:
        chol = st.text_input('Serum cholestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Suagr > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
        
    with col3:
        exang = st.text_input('Exercise-induced angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Number of major vessels (0–3) colored by fluoroscopy')
        
    with col1:
        thal = st.text_input('Thalassemia')
        
    
    
    #code for prediction
    heart_diagnosis = ''
    
    #creating a button 
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]])
        
        if(heart_prediction[0] == 1):
            heart_diagnosis = "The Person have Heart Disease"
        else:
            heart_diagnosis = "The Person do not have Heart Disease"
            
    st.success(heart_diagnosis)
    
if(selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    # Create columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
    with col2:
        Jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    
    with col3:
        RAP = st.text_input('MDVP:RAP')
    
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
    
    with col2:
        DDP = st.text_input('Jitter:DDP')
    
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
    
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
    
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
    
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    
    with col3:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')
    
    with col2:
        RPDE = st.text_input('RPDE')
    
    with col3:
        DFA = st.text_input('DFA')
    
    with col1:
        spread1 = st.text_input('spread1')
    
    with col2:
        spread2 = st.text_input('spread2')
    
    with col3:
        D2 = st.text_input('D2')
    
    with col1:
        PPE = st.text_input('PPE')
    
    # Prediction
    parkinsons_diagnosis = ''
    
    if st.button('Parkinson\'s Test Result'):
        input_data = [float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_abs),
                      float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                      float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                      float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
    
        parkinson_prediction = parkinsons_model.predict([input_data])
        
        if parkinson_prediction[0] == 1:
            parkinsons_diagnosis = "The Person has Parkinson's Disease"
        else:
            parkinsons_diagnosis = "The Person does not have Parkinson's Disease"
    
    st.success(parkinsons_diagnosis)
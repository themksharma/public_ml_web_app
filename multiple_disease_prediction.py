# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 07:32:40 2023

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:33:10 2023

@author: DELL
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('D:\Work\deployment\diabetes_model.sav', 'rb'))
kyphosis_model = pickle.load(open('D:\Work\deployment\kyphosis_model.sav', 'rb'))
heart_disease_model = pickle.load(open('D:\Work\deployment\heart_Disease.sav', 'rb'))
breast_cancer_model = pickle.load(open('D:\Work\deployment\cancer_model.sav', 'rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Kyphosis Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','person','heart','file-medical'],
                          default_index=0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction ')
    
    
    # getting the input data from the user
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
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

#kyphosis prediction page 

if(selected == 'Kyphosis Prediction'):
    st.title('Kyphosis Prediction using ML')
    
    col1 , col2 , col3 = st.columns(3)
    with col1:
        Number = st.text_input('Number')
    with col2:
        start = st.text_input('Start')
    with col3:
        Age = st.text_input('Age')
        
# code for Prediction
    Kyphosis_diagnosis = ''

# creating a button for Prediction

    if st.button('Kyphosis Test Result'):
        Kyphosis_prediction = kyphosis_model.predict([[Number,start,Age]])
     
        if(Kyphosis_prediction[0] == 1):
            Kyphosis_diagnosis = 'The person is suffering from Kyphosis'
        else:
            Kyphosis_diagnosis = 'The person is not Suffering from Kyphosis'
    
    st.success(Kyphosis_diagnosis)

#heart disease prediction

if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
#Breast Cancer Prediction

if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        meanradius = st.text_input('Mean Radius')
        
    with col2:
        meantexture = st.text_input('Mean Texture')
        
    with col3:
        meanperimeter = st.text_input('Mean Perimeter')
        
    with col1:
        meanarea = st.text_input('Mean Area')
        
    with col2:
        meansmoothness = st.text_input('Mean Smoothness')
        
    with col3:
        meancompactness = st.text_input('Mean Compactness')
        
    with col1:
        meanconcavity = st.text_input('Mean Concavity')
        
    with col2:
        meanconcavepoints = st.text_input('Mean Concave Points')
        
    with col3:
        meansymmetry = st.text_input('Mean Symmetry')
        
    with col1:
        meanfractaldimension = st.text_input('Mean Fractal Dimension')
     
    with col2:
        radiuserror = st.text_input("Radius Error")
        
    with col3:
        textureerror = st.text_input("texture error")
        
    with col1:
        perimetererror = st.text_input("perimeter error")
        
    with col2:
        areaerror = st.text_input("Area Error")
        
    with col3:
        smoothnesserror = st.text_input("Smoothness Error")
        
    with col1:
        compactnesserror = st.text_input("Compactness Error")
        
    with col2:
        concavityerror = st.text_input("Concavity error")
        
    with col3 :
        concavepointserror = st.text_input("Concave Points Error")
        
    with col1:
        symmetryerror = st.text_input("Symmetry Error")
        
    with col2:
        fractaldimensionerror = st.text_input("Fractal Dimension Error")
    
    with col3:
        worstradius = st.text_input('Worst Radius')
    
        
    with col1:
        worsttexture = st.text_input('Worst Texture')
        
    with col2:
        worstperimeter = st.text_input('Worst Perimeter')
        
    with col3:
         worstarea = st.text_input('Worst Area')
         
    with col1:
         worstsmoothness = st.text_input('Worst Smoothness')
         
    with col2:
         worstcompactness = st.text_input('Worst Compactness')
    
    with col3:
         worstconcavity= st.text_input('Worst Concavity')
         
    with col1:
         worstconcavepoints = st.text_input('Worst Concave Points')
         
    with col2:
         worstsymmetry = st.text_input('Worst Symmetry')
         
    with col3:
         worstfractaldimension= st.text_input('Worst Fractal Dimension')
        
        
     
     
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        cancer_prediction = heart_disease_model.predict([[meanradius,meantexture,meanperimeter,meanarea,meansmoothness,meancompactness,meanconcavity,meanconcavepoints,meansymmetry,meanfractaldimension,radiuserror,textureerror,perimetererror,areaerror,smoothnesserror,compactnesserror,concavityerror,concavepointserror,symmetryerror,fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstsmoothness,worstcompactness,worstconcavity,worstconcavepoints,worstsymmetry,worstfractaldimension]])                          
        
        if (cancer_prediction[0] == 1):
          breast_cancer_diagnosis = 'The person is suffering from breast cancer'
          
        else:
          breast_cancer_diagnosis = 'The person is not suffering from breast cancer'
        
    st.success(breast_cancer_diagnosis)
        



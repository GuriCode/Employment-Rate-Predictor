#!/usr/bin/env python
import streamlit as st 
import pickle
import pandas as pd

def load_model():
    with open('Employment.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
def load_data_pipe():
    with open('data_pipe.pkl', 'rb') as file:
        data = pickle.load(file)

    return data 

model=load_model()
data_pipe=load_data_pipe()   
def  show_employment_page():
    st.title('Employment Rate Prediction App')

    gender=st.selectbox('Gender',['M','F','Other'])

    ssc_b=st.selectbox('SSC_Board',['Central','Others'])

    ssc_p=st.slider('SSC_Percentage',
        1,100,1)
    hsc_b=st.selectbox('HSC_Board',['Central','Others'])


    hsc_p=st.slider('HSC_Percentage',
        1,100,1)

    hsc_s=st.selectbox('HSC_Subject',['Commerce','Arts','Science'])

    degree_p=st.slider('Degree_Percentage',
        0,100,5)
    degree_t=st.selectbox('Degree Type',['Comm&Mgmt','Sci&Tech'])
    workex=st.selectbox('Work Experienced',['Yes','No'])
    etest_p=st.slider('E Litmus Percentage',
        0,100,5)
    specialisation=st.selectbox('Specialisation',['Mkt&HR','Mkt&Fin']),
    mba_p=st.slider('MBA Percentage',
        0,100,5)


    data=pd.DataFrame({'gender': [gender],
    'ssc_p': [ssc_p],
    'ssc_b':[ssc_b],
    'hsc_p': [hsc_p],
    'hsc_b':[hsc_b],
    'hsc_s':[hsc_s],
    'degree_p':[degree_p],
    'degree_t': [degree_t],
    'workex': [workex],
    'etest_p':[etest_p],
    'specialisation':[specialisation],
    'mba_p':[mba_p]
    })

    x=pd.DataFrame(data=data_pipe.transform(data),
        columns=['cat_pipe__gender_M',
 'cat_pipe__ssc_b_Central',
 'cat_pipe__hsc_b_Others',
 'cat_pipe__hsc_s_Commerce',
 'cat_pipe__hsc_s_Science',
 'cat_pipe__degree_t_Comm&Mgmt',
 'cat_pipe__degree_t_Sci&Tech',
 'cat_pipe__workex_No',
 'cat_pipe__specialisation_Mkt&Fin',
 'num_pipe__ssc_p',
 'num_pipe__hsc_p',
 'num_pipe__degree_p',
 'num_pipe__etest_p',
 'num_pipe__mba_p'])
    
    data

    predictions=model.predict(x)

    
    st.write('Predicted with above characteristics is :',
        predictions)


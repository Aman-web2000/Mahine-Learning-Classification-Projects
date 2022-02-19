from ast import increment_lineno
from turtle import width
import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import pickle
from PIL import Image
import os.path
from pathlib import Path

plt.style.use('fivethirtyeight')



## Creating Pages 
next = st.sidebar.button('Next on list')

new_choice=["About",'Facts','Prediction']

if os.path.isfile('next.p'):
    next_clicked = pickle.load(open('next.p', 'rb'))
    
    if next_clicked == len(new_choice):
        next_clicked = 0 
else:
    next_clicked = 0

if next:
    next_clicked = next_clicked +1
    if next_clicked == len(new_choice):
        next_clicked = 0 

choice = st.sidebar.radio("go to",("About",'Facts','Prediction'), index=next_clicked)

pickle.dump(new_choice.index(choice), open('next.p', 'wb'))

## Importing Images
image='https://static.toiimg.com/photo/88203915/Stwer_Titanic.jpg?width=748&resize=4'


pickle_in=open('Titanic.pkl','rb')
clf=pickle.load(pickle_in)

## Prediciton function
def predictor(l):
    prediction=clf.predict([l])
    return prediction[0]


## WEb page
def main():
    
    if choice=='About':
        project_title='''
        <div style='background-color:#459283;padding:10px'>
        <h1 style='color:white;font:bolder;text-align:center;'>Titanic Survival Project</h1>
        </div>
        '''
        st.markdown(project_title,unsafe_allow_html=True)
        st.image(image)
        st.write('''
        The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS 
Titanic sank after colliding with an iceberg. Unfortunately, 
there weren’t enough lifeboats for everyone onboard, 
resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some 
groups of people were more likely to survive than others.

This Model predicts whether you would have survived this tragedy or not based on the data that you 
enter in the model .

Good Luck!
''')
        
    if choice=='Facts':
        html_insught_head="""
        <div style='background-color:#DAFA0C;padding:10px'>
        <h1 style='color:black;font:bolder;text-align:center'>Insights From the Data</h1>
        """
        st.markdown(html_insught_head,unsafe_allow_html=True)
        html_insights=''' <ol>
    <h4>==> Maximum number of passengers in titanic was from `3rd class` </h4>
    <h4>==> Only `33.94%` of the passengers survived  </h4>
    <h4>==> Only `33.94%` of the passengers survived  </h4>
    <h4>==> `64%` of the total pasangers were `Male`  </h4>
    <h4>==>  Most of the pasengers belongs to `15-35` years age group </h4>
    <h4>==>  Maximum people were travelling `Solo` </h4>
    <h4>==>  most of the passengers are in `S` embarked </h4>
    <h4>==>  More than `50%` of passengers were in Cabin` B` and `C` </h4>
    <h4>==>  `T` has the least number of passenger </h4>
    <h4>==>  Approx `70%` of the passengers were `Married` </h4>
    <h4>==>  Passengers in `C` emabarked has highest survival rate </h4>
    <h4>==>  `Females` has more survival rate than man </h4>
    <h4>==>  People with `1 companion` aboard has more survival rate than others </h4>
    <h4>==>  most of the people who survived are from `1st class` and maximum number of people died were from `3rd class`  </h4>
    <h4>==>  Married Passengers had `less` chance of surviving </h4>
    <h4>==> Passenger travelling with upto `3 members` had more chances of survivng </h4>
    </ol>
        '''    
        st.markdown(html_insights,unsafe_allow_html=True)
    
    
    elif choice=='Prediction':
        html_heading = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Prediction </h2>
    </div>
    """
        st.markdown(html_heading,unsafe_allow_html=True)
        st.subheader('Enter the Data Below :')
        Pclass= st.selectbox("Passenger Class",['1','2','3'])
        Age= st.slider("Age",min_value=2,max_value=80,step=2)
        fare= st.slider("Fare",min_value=10,max_value=1000,step=40)
        no_of_family_members= st.slider("No of Fmaily members on ship",min_value=0,max_value=20,step=1)
        sex= st.radio('Sex',['Male','Female'])
        Married= st.radio("Married",['Yes',"No"])
        Embarked= st.selectbox("Embarked",['S','C','Q'])
        l=[Pclass,Age,fare,no_of_family_members,sex,Married,Embarked]

        if st.button("Predict"):
            if l[0]=='1':
                l[0]=3
            elif l[0]=='3':
                l[0]=1
            elif l[0]=='2':
                l[0]=2

            if l[4]=='Male':
                l[4]=1
            elif l[4]=='Female':
                l[4]=0
    
            if l[5]=='Yes':
                l[5]=1
            elif l[5]=='No':
                l[5]=0
    

            if l[-1]=='C':
                del l[-1]
                l.append(0)
                l.append(0)
            elif l[-1]=='Q':
                del l[-1]
                l.append(1)
                l.append(0)
            elif l[-1]=='S':
                del l[-1]
                l.append(0)
                l.append(1)
            
            ans=predictor(l)
            if ans==1:
                survived="""
                <div style="background-color:#0CFA4F;padding:10 px">
                <h2 style="color:white;font:bolder;text-align:center">Congratulations! You survived</h2>
                </div>
                """
                st.markdown(survived,unsafe_allow_html=True)

            else:
                not_survived="""
                <div style="background-color:#900C3F;padding:10 px">
                <h2 style="color:white;font:bolder;text-align:center">R.I.P</h2>
                </div>
                """
                st.markdown(not_survived,unsafe_allow_html=True)




if __name__== "__main__":
    main()
import streamlit as st 
import numpy as np
import pandas as pd
import pickle
from PIL import Image

pickle_in=open('Titanic.pkl','rb')
clf=pickle.load(pickle_in)

def predictor(l):
    prediction=clf.predict([l])
    return prediction[0]

## Background Image
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F28%2F2016%2F09%2FRussian-Wreck-Zabagad-SHIPS0816-2000.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


# Side bar Design 

html_sidebar_heading="""
<div style='background-color:#0b2038;'>
<h1 style="color: white; text-align: center">Prediction</h1>
</div>
"""

st.sidebar.markdown(html_sidebar_heading,unsafe_allow_html=True)

st.sidebar.subheader('Enter the Data Below :')

Pclass= st.sidebar.selectbox("Passenger Class",['1','2','3'])
Age= st.sidebar.slider("Age",min_value=2,max_value=80,step=2)
fare= st.sidebar.slider("Fare",min_value=10,max_value=1000,step=40)
no_of_family_members= st.sidebar.slider("No of Fmaily members on ship",min_value=0,max_value=20,step=1)
sex= st.sidebar.radio('Sex',['Male','Female'])
Married= st.sidebar.radio("Married",['Yes',"No"])
Embarked= st.sidebar.selectbox("Embarked",['S','C','Q'])

l=[Pclass,Age,fare,no_of_family_members,sex,Married,Embarked]

# Main Page 

def main():

    html_page_title="""
    <div style="background-color: red;">
    <h1 style="text-align: center; color: white;">Titanic Survival Prediction</h1>
    </div>
    """

    st.markdown(html_page_title,unsafe_allow_html=True)

    image_path='https://digitaldomain.com/wp-content/uploads/2019/09/Titanic_2.jpg'
    st.image(image_path)
    
    html_about='''<div style="background-color: black; padding: 10px;">
    <p style="text-align: center; color: aliceblue;">The sinking of the Titanic is one of the most infamous shipwrecks in history.
    <br>
    <br>
    On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS 
    Titanic sank after colliding with an iceberg. Unfortunately, 
    there weren’t enough lifeboats for everyone onboard, 
    resulting in the death of 1502 out of 2224 passengers and crew.
    <br>
    <br>
    While there was some element of luck involved in surviving, it seems some 
    groups of people were more likely to survive than others.
    <br>
    <br>
    This Model predicts whether you would have survived this tragedy or not based on the data that you 
    enter in the model .
    <br>
    <br>
    Good Luck!</p>
    </div>'''

    st.markdown(html_about,unsafe_allow_html=True)


    if st.sidebar.button("Predict"):
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
                survive="""
                <div style="background-color: #4508EF;padding: 10px;">
                <h1 style="text-align: center; color: white;">Hurrah! 👏 You have Survived the Titanic</h1>
                </div>
                """
                st.markdown(survive,unsafe_allow_html=True)
            else:
                not_survived="""
                <div style="background-color: #900C3F; padding: 10px ">
                <h1 style="color: White; text-align: center;">R.I.P ☠️</h1>
                </div>
                """
                st.markdown(not_survived,unsafe_allow_html=True)

if __name__=="__main__":
    main()

from ast import increment_lineno
import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import pickle
from PIL import Image
import os.path

plt.style.use('fivethirtyeight')



## Creating Pages 
next = st.sidebar.button('Next on list')

new_choice=["About",'Vizualization','Insights','Prediction']

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

choice = st.sidebar.radio("go to",("About",'Vizualization','Insights','Prediction'), index=next_clicked)

pickle.dump(new_choice.index(choice), open('next.p', 'wb'))

## Importing Images
image=Image.open("A:\DS ML\Titanic Survival Prediction\Stöwer_Titanic.jpg")

pickle_in=open('Titanic.pkl','rb')
clf=pickle.load(pickle_in)

## Importing Data Set
df=pd.read_csv(r'A:\DS ML\Titanic Survival Prediction\new_df.csv')
cat_cols=[col for col in df.columns if df[col].dtype=='O']
num_cols=[col for col in df.columns if df[col].dtype!='O']

## Prediciton function
def predictor(l):
    prediction=clf.predict([l])
    return prediction[0]

## For Data Vizualization
def count_plot(i):
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x =i, data = df)
    st.pyplot(fig)

def hist_plot(i):
    fig = plt.figure(figsize=(10, 4))
    sns.histplot(x =i, data = df)
    st.pyplot(fig)

def box_plot(i,j):
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x =i,y=j, data = df)
    st.pyplot(fig)

def line_plot(i):
    fig = plt.figure(figsize=(10, 4))
    sns.lineplot(x =i, data = df)
    st.pyplot(fig)

def scatter_plot(i,j):
    fig = plt.figure(figsize=(10, 4))
    sns.scatterplot(x =i,y=j, data = df)
    st.pyplot(fig)


## WEb page
def main():
    
    if choice=='About': 
        st.title("Titanic Survival Model")
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
        
    if choice=='Insights':
        st.title("Insights drawn from the Data")
        file=open("A:\DS ML\Titanic Survival Prediction\Insights.html")
        line=file.readlines()
        for i in line:
            print(st.markdown(i),end=' ')    
    
    elif choice=='Vizualization':

        st.title('Vizualizing Data')

        graph=st.selectbox('Plot',['Countplot','Boxplot','Lineplot','Histogram','Scatterplot'])
        
        i=st.selectbox('Categorical Features',cat_cols)
        j=st.selectbox('Numerical features',num_cols)

        if graph=='Countplot':
            count_plot(i)
        elif graph=='Boxplot':
            box_plot(i,j)
        elif graph=='Histogram':
            hist_plot(i)
        elif graph=='Scatterplot':
            scatter_plot(i,j)

        
    
    elif choice=='Prediction':
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
            st.write(l)
            st.write(ans)
            if ans==1:
               st.subheader("Hurrah! You would have Survived the Titanic")
            else:
                st.subheader("R.I.P")




if __name__== "__main__":
    main()
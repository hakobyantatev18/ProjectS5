import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv("../dataSets/tmpSynthetic.csv")

    df = df.dropna()
    df.isna().sum().sum()

    df.duplicated()
    df.drop_duplicates()
    
    return df

def load_original():
    originalData = pd.read_csv("../dataSets/Time management data.csv")
    originalData = originalData.drop("Number",axis=1)
    originalData = originalData.drop("Nationality",axis=1)
    originalData = originalData.drop("Scores",axis=1)

    originalData = originalData.dropna()
    originalData.isna().sum().sum()

    originalData.duplicated()
    originalData.drop_duplicates()
    
    return originalData
    

df = load_data()
data = load_original()

def show_explore_page():
    #statistics
    st.title("Explore Time Management Statistics")
    
    course_counts = df['Course'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(course_counts, labels=course_counts.index, autopct="%1.1f%%", shadow=True, startangle=90,labeldistance=1.2)
    ax.axis("equal")  
    st.write("### Number of data from different courses")
    st.pyplot(fig)
    
    
    #another charts
    st.write("### Scores based on attendance")

    plt.figure(figsize=(8, 6))
    plt.bar(data['Attendance'], data['Score Range'], color='skyblue')
    plt.xlabel('Attendance Level')
    plt.ylabel('Predicted Score')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    
    
    st.write("### Scores based on attendance")
    plt.figure(figsize=(8, 6))
    plt.plot(data['Course'], data['Academic'], marker='o', linestyle='-')
    plt.xlabel('Attendance Level')
    plt.ylabel('Predicted Score')
    plt.title('Attendance vs Predicted Scores')
    plt.xticks(rotation=45)
    st.pyplot(plt)




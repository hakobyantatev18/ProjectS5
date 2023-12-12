import streamlit as st
import pandas as pd
import joblib




model = joblib.load("../jupyter/best_model.joblib")
label_encoders = joblib.load("../jupyter/encoders.joblib")
# label_encode_columns = joblib.load("fit.joblib")
# decode_label = joblib.load("decode_label.joblib")

def show_predict_page():
    st.title("Time Management Efficiency Testing")

    st.write("""### We need some info to predict you efficiency level""")

    age = (
        '<18',
        '18-20',
        '21-25',
        '26-30',
        '31-35',
        '>36'
    )
    
    gender = (
        "M",
        "F"
    )
    
    program = (
        'PM',
        'IYO',
        'FC',
        'Language',
    )
    
    course = (
        'Science and engineering',
        'Law/Legal studies',
        'Business',
        'Art and Design',
        'Computing',
        'Social Sciences and Humanities',
        'Media and Communications'
    )
    
    english = (
        '40%~49%',
        '50%~59%',
        '60%~70%',
        '>70%',
    )
    
    academic = (
        '<40%',
        '40%~49%',
        '50%~59%',
        '60%~70%',
        '>70%'
    )
    
    attendance = (
        'S0',
        'S1',
        'S2',
        'S3',
        'S4'
    )
    
    six =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    seven =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    eight =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    
    nine =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    ten =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    eleven =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    twelve =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    thirteen =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    fourteen =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    fifteen =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    sixteen =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    seventeen =(
        'Strong Agree',
        'Agree',
        'Neither',
        'Disagree',
        'Strong Disagree'
    )
    
    age = st.selectbox("Age Range",age,index=None,placeholder="Select Age Range....")
    gender = st.selectbox("Gender",gender,index=None,placeholder="Select Gender....")
    program = st.selectbox("Program",program,index=None,placeholder="Select Program....")
    course = st.selectbox("Course",course,index=None,placeholder="Select Course....")
    english = st.selectbox("Level of English",english,index=None,placeholder="Select The Level of English....")
    academic = st.selectbox("Academic Level",academic,index=None,placeholder="Select Academic Level....")
    attendance = st.selectbox("Attendance(S0 : Most attendance - S4 : Least attendance)",attendance,index=None,placeholder="Select Attendance....")
    six = st.selectbox("You often feel that your life is aimless, with no definite purpose",six,index=None,placeholder="Select....")
    seven = st.selectbox("You never have trouble organizing the things you have to do?",seven,index=None,placeholder="Select....")
    eight = st.selectbox("Once you've started an activity, you persist at it until you've completed it",eight,index=None,placeholder="Select....")
    nine = st.selectbox("Sometimes you feel that the things you have to do during the day just don't seem to matter",nine,index=None,placeholder="Select....")
    ten = st.selectbox("You will plan your activities from day to day",ten,index=None,placeholder="Select....")
    eleven = st.selectbox("You tend to leave things to the last minute?",eleven,index=None,placeholder="Select....")
    twelve = st.selectbox("You tend to change rather aimlessly from one activity to another during the day.",twelve,index=None,placeholder="Select....")
    thirteen = st.selectbox("You give up the things that you planning to do just because your friend says no.",thirteen,index=None,placeholder="Select....")
    fourteen = st.selectbox("You think you do enough with your time.",fourteen,index=None,placeholder="Select....")
    fifteen = st.selectbox("You are easy to get bored with your day-today activities.",fifteen,index=None,placeholder="Select....")
    sixteen = st.selectbox("The important interests/activities in your life tend to change frequently.",sixteen,index=None,placeholder="Select....")
    seventeen = st.selectbox("You know how much time you spend on each of the homework I do.",seventeen,index=None,placeholder="Select....")
    
    def label_encode_columns_w_fit_encoders(result, columns, encoders):
        for col in columns:
            le = encoders.get(col)
            result[col] = le.transform(result[col])
        return result
    
    
    def decode_label(column, label, encoders):
        le = encoders.get(column)
        decoded_label = le.inverse_transform([label])
    
        return decoded_label[0]
    
    def predict():
        input_data = {'Age': age,
        'Gender': gender,
        'Program': program,
        'Course': course,
        'English': english,
        'Academic' : academic,
        'Attendance' : attendance,
        '6'  : six,
        '7'  : seven,
        '8'  : eight,
        '9'  : nine,
        '10' : ten,
        '11' : eleven,
        '12' : twelve,
        '13' : thirteen,
        '14' : fourteen,
        '15' : fifteen,
        '16' : sixteen,
        '17' : seventeen,
        'Score Range' : '35-45'
        }
        input_data
    
        col_list_obj = ['Age','Gender','Program','Course','English','Academic','Attendance','6','7','8','9','10','11','12','13','14','15','16','17','Score Range']
        # input_col_list = col_list_obj[:-1]
        input_df = pd.DataFrame([input_data])
        input_encoded = label_encode_columns_w_fit_encoders(result=input_df, columns=col_list_obj, encoders=label_encoders)
    
        input_restored = input_encoded.drop('Score Range', axis=1)
        predicted_label = model.predict(input_restored)
    
        decoded_label = decode_label('Score Range', predicted_label[0], label_encoders)
        
        if decoded_label == '45+':
            st.success(":blue[Excellent] time management skills!:clapping hands:")
        elif decoded_label == '35-45':
            st.success(":blue[Good] time management skills. Need of improvement.:thumbsup:")
        elif decoded_label == '25-35':
            st.success(":red[Horrible] time management skills. In need of major improvements.:thumbsdown:")
    
    
    st.button("Predict",on_click=predict)
    
    
    
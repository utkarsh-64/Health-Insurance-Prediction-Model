import streamlit as st
import pandas as pd
import joblib

# Load the trained model
lr = joblib.load("lr.cnn")

# Define a function to take user inputs and make predictions
def predict_insurance_claim(age, sex, weight, bmi, diseases, dependents, smoker, city, blood_pressure, diabetes, exercise, job):
    # Create a dictionary with the sample data
    sample_data = {
        'age': [age],
        'sex': [sex],
        'weight': [weight],
        'bmi': [bmi],
        'hereditary_diseases': [diseases],
        'no_of_dependents': [dependents],
        'smoker': [smoker],
        'city': [city],
        'bloodpressure': [blood_pressure],
        'diabetes': [diabetes],
        'regular_ex': [exercise],
        'job_title': [job]
    }
    
    # Convert the input data into a DataFrame
    sample = pd.DataFrame(sample_data)
    
    # Make prediction
    claim = lr.predict(sample)
    
    return claim

# City options and their numerical values
cities_options = ['NewYork', 'Boston', 'Phildelphia', 'Pittsburg', 'Buffalo', 'AtlanticCity', 'Portland', 'Cambridge', 'Hartford', 'Springfield', 'Syracuse', 'Baltimore', 'York', 'Trenton', 'Warwick', 'WashingtonDC', 'Providence', 'Harrisburg', 'Newport', 'Stamford', 'Worcester', 'Atlanta', 'Brimingham', 'Charleston', 'Charlotte', 'Louisville', 'Memphis', 'Nashville', 'NewOrleans', 'Raleigh', 'Houston', 'Georgia', 'Oklahoma', 'Orlando', 'Macon', 'Huntsville', 'Knoxville', 'Florence', 'Miami', 'Tampa', 'PanamaCity', 'Kingsport', 'Marshall', 'Mandan', 'Waterloo', 'IowaCity', 'Columbia', 'Indianapolis', 'Cincinnati', 'Bloomington', 'Salina', 'KanasCity', 'Brookings', 'Minot', 'Chicago', 'Lincoln', 'FallsCity', 'GrandForks', 'Fargo', 'Cleveland', 'Canton', 'Columbus', 'Rochester', 'Minneapolis', 'JeffersonCity', 'Escabana', 'Youngstown', 'SantaRosa', 'Eureka', 'SanFrancisco', 'SanJose', 'LosAngeles', 'Oxnard', 'SanDeigo', 'Oceanside', 'Carlsbad', 'Montrose', 'Prescott', 'Fresno', 'Reno', 'LasVegas', 'Tucson', 'SanLuis', 'Denver', 'Kingman', 'Bakersfield', 'Mexicali', 'SilverCity', 'Pheonix', 'SantaFe', 'Lovelock']
cities_values = [55,  5, 63, 64,  8,  1, 65,  9, 29, 79, 81,  3, 89, 83, 85, 86, 67, 28, 56, 80, 88,  0,  6, 12, 13, 42, 47, 53, 54, 68, 30, 26, 58, 59, 44, 31, 38, 24, 49, 82, 61, 37, 46, 45, 87, 33, 17, 32, 15,  4, 71, 35,  7, 51, 14, 40, 22, 27, 23, 16, 10, 18, 70, 50, 34, 20, 90, 77, 21, 73, 74, 41, 60, 72, 57, 11, 52, 66, 25, 69, 39, 84, 75, 19, 36,  2, 48, 78, 62, 76, 43]
city_options_map = dict(zip(cities_options, cities_values))

# Job title options and their numerical values
job_titles_options = ['Actor', 'Engineer', 'Academician', 'Chef', 'HomeMakers', 'Dancer', 'Singer', 'DataScientist', 'Police', 'Student', 'Doctor', 'Manager', 'Photographer', 'Beautician', 'CA', 'Blogger', 'CEO', 'Labourer', 'Accountant', 'FilmDirector', 'Technician', 'FashionDesigner', 'Architect', 'HouseKeeper', 'FilmMaker', 'Buisnessman', 'Politician', 'DefencePersonnels', 'Analyst', 'Clerks', 'ITProfessional', 'Farmer', 'Journalist', 'Lawyer', 'GovEmployee']
job_titles_values = [ 2, 16,  0, 10, 22, 12, 32, 13, 30, 33, 15, 28, 29,  5,  8,  6,  9, 26,  1, 19, 34, 18,  4, 23, 20,  7, 31, 14,  3, 11, 24, 17, 25, 27, 21]
job_titles_map = dict(zip(job_titles_options, job_titles_values))

# Homepage
def homepage():
    st.title('Insurance Claim Prediction')
    st.write("""
    Welcome to the Insurance Claim Prediction App! 
    Use this app to predict the insurance claim amount based on various factors.
    """)

    st.subheader('About the Predictor')
    st.write("""
    Welcome to our Health Insurance Cost Predictor, where accuracy meets simplicity. Our advanced model utilizes a comprehensive dataset including factors such as age, sex, weight, BMI, hereditary diseases, number of dependents, smoking habits, city of residence, blood pressure, diabetes status, regular exercise routine, job title, and past insurance claims. With this wealth of information, our model provides precise insights into your health insurance expenses, empowering you to make informed decisions about your coverage. Take control of your financial planning today.""")
    st.image('home.jpg', use_container_width=True)

    st.subheader('More about The Model')
    st.write(""" Input your data with ease and receive estimated insurance cost of your unique profile. Our predictor utilizes advanced algorithms and a wealth of demographic and health-related factors, ensuring accuracy and reliability in every projection. Reach out to our friendly team for assistance. Start planning your financial future today with just a few clicks!" """)

# About Us page
def about_us():
    st.title('About Us')
    st.write("""
    This app is created to provide a simple interface for predicting insurance claims.
    """)

    st.subheader('Meet the Team')
    st.image('download.jpeg', use_container_width=True)
    
    
    st.write("""This Project is created by,""")
    st.write("""Utkarsh Lakhani (AIML)""")
    st.write("""Kartik Mehta (AIML)""")
    st.write("""Karan Rekhan (AIML)""")
    st.write("""We are the first year students of Symbiosis Institute if technology""")

    st.subheader('Contact US')
    st.write('''Email: utkarsh.lakhani.btech2023@sitpune.edu.in''')
    st.write(''' LinkedIn: https://www.linkedin.com/in/utkarsh-lakhani/''')
    
# Prediction page
def prediction_page():
    st.title('Predict Insurance Claim')

    # User inputs
    age = st.number_input('Enter the age of the person:', min_value=0, max_value=120, value=30)
    sex = st.radio('Sex:', ('Male', 'Female'))
    weight = st.number_input('Enter the weight of the person:', min_value=0, value=70)
    bmi = st.number_input('Enter the bmi of the person:', min_value=0.0, value=25.0)
    diseases_options = {'NoDisease': 0, 'Epilepsy': 1, 'EyeDisease': 2, 'Alzheimer': 3, 'Arthritis': 4, 'HeartDisease': 5, 'Diabetes': 6, 'Cancer': 7, 'High BP': 8, 'Obesity': 9}
    diseases = st.selectbox('Select the hereditary disease:', list(diseases_options.keys()))
    dependents = st.number_input('Enter the number of dependents:', min_value=0, value=0)
    smoker = st.radio('Is the person a smoker?', ('No', 'Yes'))
    city = st.selectbox('Select the city:', cities_options)
    blood_pressure = st.number_input('Enter the blood pressure of the person:', min_value=0, value=120)
    diabetes = st.radio('Is the person diabetic?', ('No', 'Yes'))
    exercise = st.radio('Does the person exercise regularly?', ('No', 'Yes'))
    job = st.selectbox('Select the job title:', job_titles_options)

    # Convert categorical inputs to numerical
    sex = 1 if sex == 'Male' else 0
    smoker = 1 if smoker == 'Yes' else 0
    diabetes = 1 if diabetes == 'Yes' else 0
    exercise = 1 if exercise == 'Yes' else 0
    diseases = diseases_options[diseases]
    city = city_options_map[city]
    job = job_titles_map[job]

    # Predict insurance claim on button click
    if st.button('Predict Insurance Claim'):
        claim = predict_insurance_claim(age, sex, weight, bmi, diseases, dependents, smoker, city, blood_pressure, diabetes, exercise, job)
        st.write(f'The predicted insurance claim is {claim[0]:,.2f} $.')
        

if __name__ == "__main__":
    pages = {
        "Home": homepage,
        "Claim Prediction": prediction_page,
        "About Us": about_us
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

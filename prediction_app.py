import numpy as np
import pickle
import streamlit as st

#loading the saved model
load_model = pickle.load(open('trained_model.sav', 'rb'))


# defining a predictive function
def heart_disease_prediction(HighBP, HighChol, CholCheck, BMi, Smoker, Stroke,
       Diabetes, PhysActivity, Fruits, Veggies, HvyAlcoholConsump,
       AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth,
       DiffWalk, Sex, Age, Education, Income):
    
    if HighBP == "High":
        HighBP =1
    elif HighBP == "Normal":
        HighBP = 0
    elif HighBP == "Low":
        HighBP =0
    
    if HighChol == "High":
        HighChol = 1
    elif HighChol == "Normal":
        HighChol = 0
    elif HighChol == "Low":
        HighChol =0
        
    if CholCheck == 'Yes':
        CholCheck =1
    elif CholCheck == 'No':
        CholCheck =0
    
    if Smoker == 'Yes':
        Smoker = 1
    elif Smoker == 'No':
        Smoker = 0
        
    if Stroke == 'Yes':
        Stroke = 1
    elif Stroke == 'No':
        Stroke = 0
    
    if Diabetes == 'No' or Diabetes == 'only during pregnancy':
        Diabetes = 0
    elif Diabetes == 'Pre-diabetes or borderline diabetes':
        Diabetes = 1
    elif Diabetes == 'Yes':
        Diabetes = 2
        
    if PhysActivity == 'Yes':
        PhysActivity = 1
    elif PhysActivity == 'No':
        PhysActivity = 0
        
    if Fruits == 'Yes':
        Fruits = 1
    elif Fruits == 'No':
        Fruits = 0
    
    if Veggies == "Yes":
        Veggies = 1
    elif Veggies == "No":
        Veggies = 0
        
    if HvyAlcoholConsump == 'Yes':
        HvyAlcoholConsump = 1
    elif HvyAlcoholConsump == 'No':
        HvyAlcoholConsump = 0
    
    if AnyHealthcare == "Yes":
        AnyHealthcare = 1
    elif AnyHealthcare == 'No':
        AnyHealthcare = 0
    
    if NoDocbcCost == 'Yes':
        NoDocbcCost = 1
    elif NoDocbcCost == 'No':
        NoDocbcCost = 0
    
    if GenHlth == "Poor":
        GenHlth = 1
    elif GenHlth == "Fair":
        GenHlth = 2
    elif GenHlth == "Good":
        GenHlth = 3
    elif GenHlth == "Very Good":
        GenHlth = 4
    elif GenHlth == "Excellent":
        GenHlth = 5
        
    if DiffWalk == 'Yes':
        DiffWalk = 1
    elif DiffWalk == 'No':
        DiffWalk = 0
    
    if Sex == 'Male':
        Sex = 1
    if Sex == 'Female':
        Sex = 0
    
    if Age == "18 - 24":
        Age = 1
    elif Age == "25 - 29":
        Age = 2
    elif Age == "30 - 34":
        Age = 3
    elif Age == "35 - 39":
        Age = 4
    elif Age == "40 - 44":
        Age = 5
    elif Age == "45 - 49":
        Age = 6
    elif Age == "50 - 54":
        Age = 7
    elif Age == "55 - 59":
        Age = 8
    elif Age == "60 - 64":
        Age = 9
    elif Age == "65 - 69":
        Age = 10
    elif Age == "70 - 74":
        Age = 11
    elif Age == "75 - 80":
        Age = 12
    elif Age == "Over 80":
        Age = 13
        
    if Education == "Kindergaten or did not attend school":
        Education = 1
    elif Education == "Primary or equivalent":
        Education = 2
    elif Education == "High School":
        Education = 3
    elif Education == "Tertiary or diploma or equivalent":
        Education = 4
    elif Education == "Bachelor's Degree":
        Education = 5
    elif Education == "Master's Degree, PhD or higher":
        Education = 6
    
    if Income == "Prefer not to say":
        Income = 0
    elif Income == "less than 10,000":
        Income = 1
    elif Income == "10,000 - 25,000":
        Income = 2
    elif Income == "25,001 - 35,000":
        Income = 3
    elif Income == "35,001 - 45,000":
        Income = 4
    elif Income == "45,001 - 55,000":
        Income = 5
    elif Income == "55,001 - 65,000":
        Income = 6
    elif Income == "65,001 - 75,000":
        Income = 7
    elif Income == "Over 75,000":
        Income = 8
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray([HighBP, HighChol, CholCheck, BMi, Smoker, Stroke,
       Diabetes, PhysActivity, Fruits, Veggies, HvyAlcoholConsump,
       AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth,
       DiffWalk, Sex, Age, Education, Income])

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'does not have heart disease'
    else:
        return 'has heart disease'
    
def main():

    # giving a title
    st.title('Heart Disease prediction web app, it is just a demo. Do not get scared')
    

    # setting the fields
    HighBP = st.selectbox("Blood Pressure as adviced by health professional:", ["High",
                                                                                "Normal", 
                                                                                "Low"])
    
    HighChol = st.selectbox("Cholestrol Level as adviced by health professional:", ["High",
                                                                                    "Normal", 
                                                                                    "Low"])
    
    CholCheck = st.selectbox("Have you checked your cholestrol level in the past 5 years?", ['Yes', 
                                                                                             'No'])
    
    BMi = st.number_input("Body Mass Index:", min_value=0.1, max_value=100.0, value=1.0)

    Smoker = st.selectbox("Do you smoke:", ['Yes', 
                                            'No'])
    
    Stroke = st.selectbox("Have you ever had a stroke?", ['Yes', 
                                                          'No'])
    
    Diabetes = st.selectbox("Diabetes:", ['Yes', 
                                          'No', 
                                          'only during pregnancy', 
                                          'Pre-diabetes or borderline diabetes'])
    
    PhysActivity = st.selectbox("Have you had any physical activity in the past 30 days? Other than your job", ['Yes', 
                                                                                                                'No'])
    
    Fruits = st.selectbox("At least 1 fruit a day", ['Yes', 
                                                     'No'])
    
    Veggies =  st.selectbox("At least 1 vegetable a day", ['Yes', 
                                                           'No'])
    
    HvyAlcoholConsump = st.selectbox("If male, more than 14 alcoholic drinks per week\
                                      if female, more than 7 alcoholic drinks per week", ['Yes', 
                                                                                          'No'])
    
    AnyHealthcare = st.selectbox("Do you have health insurance cover?", ['Yes', 
                                                                       'No'])
    
    NoDocbcCost =  st.selectbox("In the past 12 months, have you failed to see a doctor because of cost?", ['Yes', 'No'])
    
    GenHlth = st.selectbox("what is your general health?", ['Poor', 
                                                            'Fair', 
                                                            'Good', 
                                                            'Very Good', 
                                                            'Excellent'])
    
    MentHlth = st.number_input("In the past 30 days, how many days have you felt mentally unwell?", min_value=0, max_value=31)
    
    PhysHlth = st.number_input("In the past 30 days, how many days have you felt physically unwell?", min_value=0, max_value=31)
    
    DiffWalk = st.selectbox("Do you experience difficulty in walking or climbing stairs?", ['Yes', 
                                                                                            'No'])
    
    Sex = st.selectbox("Sex:", ['Male', 
                                'Female'])
    
    Age = st.selectbox("Age bracket:", ['18 - 24', 
                                        '25 - 29', 
                                        '30 - 34', 
                                        '35 - 39', 
                                        '40 - 44',
                                        '45 - 49', 
                                        '50 - 54', 
                                        '55 - 59', 
                                        '60 - 64', 
                                        '65 - 69',
                                        '70 - 74', 
                                        '75 - 80', 
                                        'Over 80'])
    
    Education = st.selectbox("Highest level of education:", ['Kindergaten or did not attend school',
                                                             "Primary or equivalent",
                                                             "High School",
                                                             "Tertiary or diploma or equivalent",
                                                             "Bachelor's Degree",
                                                             "Master's Degree, PhD or higher"])
    
    Income = st.selectbox("Annual Income from all sources in US Dollars:", ["Prefer not to say",
                                                                            "less than 10,000",
                                                                            "10,000 - 25,000",
                                                                            "25,001 - 35,000",
                                                                            "35,001 - 45,000",
                                                                            "45,001 - 55,000",
                                                                            "55,001 - 65,000",
                                                                            "65,001 - 75,000",
                                                                            "Over 75,000"])
    
    # Code for prediction
    diagnosis = ''
    
    # Creating a button for prediction
    if st.button("Heart disease test result"):
        diagnosis = heart_disease_prediction(HighBP, HighChol, CholCheck, BMi, Smoker, Stroke,
                                             Diabetes, PhysActivity, Fruits, Veggies, HvyAlcoholConsump,
                                             AnyHealthcare, NoDocbcCost, GenHlth, MentHlth,
                                             PhysHlth, DiffWalk, Sex, Age, Education, Income)
        
        if diagnosis == 'has heart disease':
            st.warning(diagnosis)
        else:
            st.success(diagnosis)
    

if __name__ == '__main__':
    main()
    
    
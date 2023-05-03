import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]


def show_predict_page():
    st.title("Graduation Success Percentage")

    st.write("""### We need some information to predict the Graduation Success Percentage""")

    School= ("Government Public","Private"
        
    )

    Sex = (
        "Male","Female","TransPerson"
    )

    City=(
        "Urban","Rural"
    )

    
    Jobtype=(
        "Home Maker","Health","Other","Services","Teacher"
    )
    Reason=(
        "Skill Upgradation","Family/Peer Recommendation","Course"
        ,"Other"
    )
    Guardian=(
        "Select one","Father","Other","Mother",
    )
    Backlogs=(1,2,3,0)
    Coachings=(1,0)
    Binarys=("Yes","No")
    school = st.selectbox("School", School)
    Gender = st.selectbox("Gender", Sex)
    Age = st.slider("Age", 0, 50, 3)
    City = st.selectbox("City Type", City)
    Cohabitant=st.selectbox("Parents Living Together",Binarys)
    Family_Members = st.slider("Family members", 0, 10, 1)
    Father_Job=st.selectbox("Father's Job",Jobtype)
    Mother_Job=st.selectbox("Mother's Job",Jobtype)
    Reason = st.selectbox("Reason", Reason)
    Guardian=st.selectbox("Guardian",Guardian)
    Travel_time = st.slider("Travel Time", 0, 10, 1)
    study_time = st.slider("Study Time", 0, 5, 1)
    Family_rel=st.slider("Family Relation Rating", 0, 5, 1)
    Free_time=st.slider("Free Time after Studies", 0, 5, 1)
    Backlogs=st.selectbox("Backlogs",Backlogs)
    Family_support=st.selectbox("Family support",Coachings)
    Additionals=st.selectbox("Taking additional Courses",(1,0))
    Internet_access=st.selectbox("Internet Access",Binarys)
    WeekdayParties=st.selectbox("Weekday Parties",(1,0))
    WeekendParties=st.selectbox("Weekend Parties",(1,0))
    Relationship=st.selectbox("Relationship",("Single","Married/Divorced"))
    Extra_curri=st.selectbox("Extra Curricular Activities",(1,0))
    Secondary_taken=st.selectbox("Secondary Education",(1,0))
    HigherEducation=st.selectbox("Planning for Higher Education",(1,0))
    FHealthStatus=st.slider("Health Status", 0, 5, 1)
    Goout=st.slider("GoOut with Friends", 0, 5, 1)
    SecondarySchoolabsences = st.slider("Number of School absences", 0, 90, 1)

    ok = st.button("Calculate Probability and Success")
    if ok:
        Internet_status=0

        if school=='Private':
            school_GP=0
            school_MS=1
        else:
            school_GP=1
            school_MS=0
        if Gender=='Male':
            sex_F=0
            sex_M=1
        else :
            sex_F=1
            sex_M=0
        if City=="Urban":
            address_R=0
            address_U=1
        else:
            address_R=1
            address_U=0
        
        if Family_Members>=3:
            famsize_GT3=1
            famsize_LE3=0
        else:
            famsize_GT3=0
            famsize_LE3=1
        if Cohabitant=='Yes':
            Pstatus_A=0
            Pstatus_T=1
        else:
            Pstatus_T=0
            Pstatus_A=1
        if Internet_access=='Yes':
            Internet_status=1
           
        Medu=3
        Fedu=3
        reason_course=0
        reason_home=0
        reason_other=0
        reason_reputation=0
        match Reason:
            case 'Skill Upgradation':
                reason_course=1
            case 'Family/Peer Recommendation':
                reason_home=1
            case 'Other':
                reason_other=1
        guardian_father=0
        guardian_mother=0
        guardian_other=0  
##Hardcoding as of now for skeleton for the Medu and Fedu,should be taken as inputs from the Frontend.
# Making Father as Services and Mother as Teacher
#Keeping Romantic as 1 for default

        if Guardian=='Father':
            guardian_father=1
        elif Guardian=='Mother':
            guardian_mother=1
        else:
            guardian_other=1        
        

        X = np.array([[school_GP, school_MS, sex_F, sex_M, Age, address_R,
       address_U, famsize_GT3, famsize_LE3, Pstatus_A,
       Pstatus_T, Medu, Fedu, 0, 0,
       0, 0, 1, 0,
       0, 0, 1, 0,
       reason_course, reason_home, reason_other,
       reason_reputation, guardian_father, guardian_mother,
       guardian_other, Travel_time, study_time, Backlogs,
       Additionals,  Family_support, 1, Extra_curri, Secondary_taken, HigherEducation,
       Internet_status, 1, Family_rel, Free_time, Goout, WeekdayParties,
       WeekendParties, FHealthStatus, SecondarySchoolabsences]])
        
        X = X.astype(float)

        Graduation = regressor.predict(X)
        GraduationPercent=regressor.predict_proba(X)[0:1,1]
        
        st.write(Graduation[0] +" With a probablity of of Graduating as  "+str(GraduationPercent[0]))
       
       
        #st.subheader(f"The estimated Graduation percentage is ${Graduation[0]:.2f}")
import joblib
model = joblib.load("salary_est_model.pk1") 

Experience = float( input("Enter the Experience: ") )
print("Prediceted salary in INR : " , model.predict([[Experience]])[0] , "/-" )
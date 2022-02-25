from flask import Flask , render_template,request

import math
import numpy as np
import pandas as pd
import sklearn
import requests
import pickle
  
app = Flask(__name__) #creating the Flask class object 
model = pickle.load(open('logistic_regression_model.pkl', 'rb')) 
 
@app.route('/', methods = ['POST', 'GET']) 
def home():  
    if request.method == 'POST':
      

#______________________GUI______________________________________-

        Age = int(request.form['age'])
        Embarked = int(request.form['embarked'])
        Sibsp = int(request.form['sibsp'])
        Parch = int(request.form['parch'])
        Gender = int(request.form['gender'])
        Fare = int(request.form['fare'])
        Pclass = int(request.form['pclass'])
        
      
#__________________________GUI_END_____________________________________
        print(Age, Embarked, Sibsp, Parch, Gender, Fare, Pclass)
        
        prediction = model.predict([[Pclass,Gender, Age,Sibsp,Parch,Fare,Embarked]])
        print("Final Prediction:  ",prediction)
     
        if prediction == 0:
            return render_template('index.html',prediction = "Sorry, you could not make it!" )
        if prediction == 1:
            return render_template('index.html',prediction = "Hurray, You will be saved !" )

        

    return render_template('index.html') 
  
if __name__ =='__main__':  
    app.run(debug = True, port="8000" )  
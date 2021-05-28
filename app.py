# Import necessary libraries
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify, render_template, request, g, redirect
from tensorflow.keras.models import load_model
import pandas as pd
import psycopg2
import os
# sklearn libraries need to be imported
# from sklearn.preprocessing import StandardScaler


#########################################
# Flask Setup
#########################################
app = Flask(__name__)

# Create the route that renders the index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Create a route to get the user inputs and send them to the model
@app.route("/predict", methods=['GET', 'POST'])
def predict(input):
    if request.method == 'POST':
        Admission_Deposit = request.form["Admission_Deposit"]
        Age = request.form["Age"]
        Available_Extra_Rooms_in_Hospital = request.form["Available Extra Rooms in Hospital"]
        Bed_Grade = request.form["Bed Grade"]
        City_Code_Hospital = request.form["City_Code_Hospital"]
        City_Code_Patient = request.form["City_Code_Patient"]
        Department = request.form["Department"]
        Hospital_code = request.form["Hospital_code"]
        Hospital_region_code = request.form["Hospital_region_code"]
        Hospital_type_code = request.form["Hospital_type_code"]
        Severity_of_Illness = request.form["Severity of Illness"]
        Type_of_Admission = request.form["Type of Admission"]
        Visitors_with_Patient = request.form["Visitors with Patient"]
        Ward_Facility_Code = request.form["Ward_Facilty_Code"]
        Ward_Type = request.form["Ward_Type"]

        input = {"Admission_Deposit": Admission_Deposit,
                 "Age": Age,
                 "Available Extra Rooms in Hospital": Available_Extra_Rooms_in_Hospital,
                 "Bed Grade": Bed_Grade,
                 "City_Code_Hospital": City_Code_Hospital,
                 "City_Code_Patient": City_Code_Patient,
                 "Department": Department,
                 "Hospital_code": Hospital_code,
                 "Hospital_region_code": Hospital_region_code,
                 "Hospital_type_code": Hospital_type_code,
                 "Severity of Illness": Severity_of_Illness,
                 "Type of Admission": Type_of_Admission,
                 "Visitors with Patient": Visitors_with_Patient,
                 "Ward_Facility_Code": Ward_Facilty_Code,
                 "Ward_Type": Ward_Type}
        

    translators = None
    with open('translators.json', 'r') as f:
        translators=json.load(f)

    X_translator = translators['X_translator']
    scale_translator = translators['scale_translator']
    order = translators['data_order']
    y_translator = translators['y_translator']
    input_t = {}
    for (category, value) in input.items():
        if category in x_categorical_columns:
            input_t[category] = X_translator[category][str(value)]
        elif category in x_numerical_columns:
            mean = scale_translator[category]['mean']
            std = scale_translator[category]['standard_deviation']
            value = (value - mean)/std
            input_t[category] = value
        else:
            print(f'ERROR: Unsupported parameter found! {category}') 

    input_t = np.array([input_t[i] for i in order]).reshape(1, 15)
    model_1 = create_model()
    model_1.load_weights('training_1/cp-0047.ckpt')
    prediction = model_1.predict(input_t).argmax()
    prediction = y_translator[str(prediction)]
    return render_template("predict.html", prediction=prediction)

predict(input)


if __name__ == "__main__":
    app.run() 

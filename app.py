# Import necessary libraries
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify, render_template, request, g, redirect
from tensorflow.keras.models import load_model
import pandas as pd
import psycopg2
import sqlite3
import os
# from model_files.ml_model import the-name-of-the-model
# sklearn libraries need to be imported
# from sklearn.preprocessing import StandardScaler


#########################################
# Flask Setup
#########################################
app = Flask(__name__)

#########################################
# Database setup
#########################################
# Create engine and connection
# engine = create_engine(f"postgresql://hospital-stay-postgresdb.czsgahc5qz1z.us-east-2.rds.amazonaws.com")
# conn = engine.connect()

# the model needs to be loaded and possibly the prepossesser or scaler
model = load_model(modelpath and saved-model-name)
# model = joblib.load(saved-model-name.pkl')
# sc = load(modelpath and saved-scaler-name)

# Create a test route and function that returns a string
@app.route("/test", methods=['GET'])
def test():
    return "Pinging model appplication!"


# Create the route that renders the index.html template
 @app.route("/")
def home():
    return render_template("index.html")

# Create a route to get the user inputs and send them to the model
@app.route("/predict", methods=['GET','POST'])
def predict();
    if request.method == 'POST':
        hospcode = request.form["Hospital_code"]
        hosptype = request.form["Hospital_type_code"]
        #hospcity = request.form["City_Code_Hospital"]
        hospregion = request.form["Hospital_region_code"]
        extrarooms= request.form["Available Extra Rooms in Hospital"]
        dept = request.form["Department"]
        ward = request.form["Ward_Type"]
        wardcode = request.form["Ward_Facilty_Code"]
        bedgrade = request.form["Bed Grade"]
        #patientcity = request.form["City_Code_Patient"]
        admtype = request.form["Type of Admission"]
        severity = request.form["Severity of Illness"]
        visitors = request.form["Visitors with Patient"]
        age = request.form["Age"]
        deposit = request.form["Admission_Deposit"]

# Create a dataframe that holds the user inputs and if needed run the preprocessor
    row_df = pd.DataFrame([pd.Series([hospcode, hosptype, hospregion, extrarooms, dept, ward, wardcode, bedgrade, admtype, severity, visitors, age, deposit])])
    row_df = pd.DataFrame(std.transform(row_df))

# Predict the probability and return the result
    prediction = model.predict(row_df)
    output=(prediction)

    return (result)




if __name__ == "__main__":
    app.run() 

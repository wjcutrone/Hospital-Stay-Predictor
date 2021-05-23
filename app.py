# Import necessary libraries
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify, render_template, request, g, redirect
import pandas as pd
import psycopg2
import sqlite3
# sklearn libraries need to be imported



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



# Create a test route and function that returns a string
@app.route("/test", methods=['GET'])
def test():
    return "Pinging model appplication!"


# Create the route that renders the index.html template
 @app.route("/")
def home():
    return render_template("index.html")

# Create a route to get the user input and send it to the model
@app.route("/send", methods=['GET','POST'])
def send();
    if request.method == 'POST':
        hospcode = request.form["Hospital_code"]
        hosptype = request.form["Hospital_type_code"]
        hospcity = request.form["City_Code_Hospital"]
        hospregion = request.form["Hospital_region_code"]
        extrarooms= request.form["Available Extra Rooms in Hospital"]
        dept = request.form["Department"]
        ward = request.form["Ward_Type"]
        wardcode = request.form["Ward_Facilty_Code"]
        bedgrade = request.form["Bed Grade"]
        patientcity = request.form["City_Code_Patient"]
        admtype = request.form["Type of Admission"]
        severity = request.form["Severity of Illness"]
        visitors = request.form["Visitors with Patient"]
        age = request.form["Age"]
        deposit = request.form["Admission_Deposit"]










if __name__ == "__main__":
    app.run() 

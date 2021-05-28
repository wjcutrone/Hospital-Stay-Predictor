-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/ZtNTl7
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Create the training table
CREATE TABLE "train_data" (
    "case_id" int ,
    "Hospital_code" int ,
    "Hospital_type_code" varchar(50) ,
    "City_Code_Hospital" int ,
    "Hospital_region_code" varchar(50) ,
    "Avaialbe Extra Rooms in Hospital" int ,
    "Department" varchar(100) ,
    "Ward_Type" varchar(50) ,
    "Ward_Facility_Code" varchar(50) ,
    "Bed Grade" float ,
    "patientid" int ,
    "City_Code_Patient" float ,
    "Type of Admission" varchar(100)  ,
    "Severity of Illness" varchar(100) ,
    "Visitors with Patient" float ,
    "Age" varhcar(50)  ,
    "Admission_Deposit" float ,
    "Stay" varchar(50) 
);


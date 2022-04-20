# import the necessary libaries 
import pandas as pd
import sqlite3 as db

# Read the file into a csv 
# data_frame = pd.read_csv("Spacex.csv")
# data_frame.head()

# Create connection
connection = db.connect('Space.db')

# Create database 
# data_frame.to_sql('SPACEXTBL', connection)

# TASK 1
all_launch_sites = pd.read_sql('SELECT * FROM SPACEXTBL', connection)
all_launch_sites

unique_launch_sites = pd.read_sql('SELECT DISTINCT Launch_Site FROM SPACEXTBL', connection)
unique_launch_sites

# TASK 2
records_beginning_with_cca = pd.read_sql("SELECT * FROM SPACEXTBL WHERE Launch_Site LIKE 'CCA%' LIMIT 5", connection)
records_beginning_with_cca

# TASK 3
total_mass = pd.read_sql("SELECT SUM(PAYLOAD_MASS__KG_) FROM SPACEXTBL", connection)
total_mass

# TASK 4
avg_mass = pd.read_sql("SELECT AVG(PAYLOAD_MASS__KG_) FROM SPACEXTBL", connection)
avg_mass

# TASK 5
first_successful_landing = pd.read_sql("SELECT MIN(DATE) FROM SPACEXTBL WHERE Mission_Outcome = 'Success'", connection)
first_successful_landing


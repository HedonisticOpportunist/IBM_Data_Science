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
unique_launch_sites = pd.read_sql('SELECT DISTINCT Launch_Site FROM SPACEXTBL', connection)

# TASK 2
records_beginning_with_cca = pd.read_sql("SELECT * FROM SPACEXTBL WHERE Launch_Site LIKE 'CCA%' LIMIT 5", connection)

# TASK 3
total_mass = pd.read_sql("SELECT SUM(PAYLOAD_MASS__KG_) FROM SPACEXTBL", connection)

# TASK 4
avg_mass = pd.read_sql("SELECT AVG(PAYLOAD_MASS__KG_) FROM SPACEXTBL", connection)

# TASK 5
first_successful_landing = pd.read_sql("SELECT MIN(DATE) FROM SPACEXTBL WHERE Mission_Outcome = 'Success'", connection)

# TASK 6
boosters = pd.read_sql("SELECT DISTINCT Booster_Version FROM SPACEXTBL WHERE MISSION_OUTCOME = 'Success' AND PAYLOAD_MASS__KG_ BETWEEN 4000 AND 6000", connection)

# TASK 7
total_outcomes = pd.read_sql("SELECT COUNT(Mission_Outcome) FROM SPACEXTBL", connection)

# TASK 8
booster_versions_max = pd.read_sql("SELECT Booster_Version FROM SPACEXTBL WHERE PAYLOAD_MASS__KG_=(SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEXTBL)", connection)

# TASK 9 
failed_outcomes_drone = pd.read_sql("SELECT DATE, MISSION_OUTCOME, BOOSTER_VERSION, LAUNCH_SITE FROM SPACEXTBL WHERE DATE LIKE '%2015%'", connection)

# TASK 1
static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
# print(response.status_code)

# Use json_normalize meethod to convert the json result into a dataframe
response_into_json = response.json()

# json into data frame 
data_frame = pd.json_normalize(response.json())

# Get the head of the dataframe
data = data_frame.head(5)

# Create a data from launch_dict
launch_df = pd.DataFrame.from_dict(launch_dict)

# Show the head of the dataframe
launch_df.describe()

# TASK 2
# Filter to only display Falcon 9 launches 
data_falcon9 = launch_df[launch_df['BoosterVersion']!='Falcon 1']

# TASK 3
# Calculate the mean value of PayloadMass column
mean_value = data_falcon9['PayloadMass'].mean() 

data_falcon9['PayloadMass'].fillna(mean_value, inplace=True)
data_falcon9.isnull().sum()

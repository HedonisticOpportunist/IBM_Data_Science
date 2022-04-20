# TASK 1

static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
# print(response.status_code)

# Use json_normalize meethod to convert the json result into a dataframe
response_into_json = response.json()

# json into data frame 
data_frame = pd.json_normalize(response_into_json)

# Get the head of the dataframe
data = data_frame.head(5)

# Create a data from launch_dict
revised_df = pd.DataFrame.from_dict(launch_dict, orient='index', dtype=None).dropna()

# Show the head of the dataframe
revised_df.describe()

# Filter to only display Falcon 9 launches 
data_falcon9 = revised_df['BoosterVersion' != 'Falcon 1']

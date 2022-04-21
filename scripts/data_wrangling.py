# TASK 1
# Apply value_counts() on column LaunchSite
df['LaunchSite'].value_counts()

# TASK 2
# Apply value_counts on Orbit column
df['Orbit'].value_counts()

# TASK 3
landing_outcomes = df['Outcome'].value_counts()

# TASK 4
empty_list = []

landing_class = None

for item in df['Outcome']:
    if item in bad_outcomes:
        landing_class = 0
    else:
        landing_class = 1

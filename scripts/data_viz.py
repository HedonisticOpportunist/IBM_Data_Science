# TASK 1
# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.catplot(y='LaunchSite', x='FlightNumber', hue='Class', data=df, aspect=2)
plt.xlabel("Flight Number", fontsize=20)
plt.ylabel("Launch site", fontsize=20)
plt.show()

# TASK 2
# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.scatterplot(x='PayloadMass', y='LaunchSite', hue='Class', data=df)
plt.xlabel("Payload Mass kg", fontsize=20)
plt.ylabel("Launch Site", fontsize=20)
plt.show()

# TASK 4
# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value
sns.catplot(x="FlightNumber", y="Orbit", hue='Class' , data=df, aspect=2)
plt.xlabel("Flight Number", fontsize=15)
plt.ylabel("Orbit", fontsize=15)
plt.show()

# TASK 5
# Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value
sns.catplot(x="PayloadMass", y="Orbit", hue='Class' , data=df,aspect=2)
plt.xlabel("Payload mass", fontsize=15)
plt.ylabel("Orbit", fontsize=15)
plt.show()

# TASK 7
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features_one_hot = pd.get_dummies(features, columns=["Orbit","LaunchSite","LandingPad","Serial"])

# TASK 8 
features_one_hot=features_one_hot.astype("float64")

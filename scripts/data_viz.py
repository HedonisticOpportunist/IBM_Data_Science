# TASK 1
# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.catplot(y='LaunchSite', x='FlightNumber', hue='Class', data=df, aspect=2)
plt.xlabel("Flight Number", fontsize=20)
plt.ylabel("Launch site", fontsize=20)
plt.show()

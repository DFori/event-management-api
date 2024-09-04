import matplotlib.pyplot as plt

# Pie chart data
labels = ['Disapprove', 'Approve', 'Undecided']
sizes = [56, 27, 17]
colors = ['orange', 'blue', 'green']

# Bar chart data
labels_bar = ['Over 65', '50-65', '35-49', 'Under 35']
sizes_bar = [6, 7, 54, 33]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
ax1.axis('equal')  

# Bar chart
ax2.bar(labels_bar, sizes_bar, color='skyblue')
ax2.set_ylabel('Percentage')
ax2.set_title('Age of Approvers')

# Show the plot
plt.show()
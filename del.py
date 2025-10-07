import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'factory': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'status': ['Unhealthy', 'Healthy', 'Unhealthy', 'Unhealthy', 'Healthy', 'Unhealthy', 'Unhealthy']
}

df = pd.DataFrame(data)

# Create 'Unhealthy' measure (10 mins per Unhealthy status)
df['Unhealthy'] = df['status'].apply(lambda x: 10 if x == 'Unhealthy' else 0)

# Group by factory and sum Unhealthy minutes
downtime_per_factory = df.groupby('factory')['Unhealthy'].sum().reset_index()

# Plot the bar chart
plt.figure(figsize=(8, 5))
plt.bar(downtime_per_factory['factory'], downtime_per_factory['Unhealthy'], color='red')
plt.title('Down Time per Factory')
plt.xlabel('Factory')
plt.ylabel('Down Time (minutes)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Show the plot
plt.show()

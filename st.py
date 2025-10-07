import pandas as pd

# Sample data
data = {
    'timestamp': ['2025-08-25 10:00', '2025-08-25 10:10', '2025-08-25 10:20', '2025-08-25 10:30'],
    'status': ['Healthy', 'Unhealthy', 'Healthy', 'Unhealthy']
}

df = pd.DataFrame(data)

# Create the "Unhealthy" measure
df['Unhealthy'] = df['status'].apply(lambda x: 10 if x == 'Unhealthy' else 0)

# View the result
print(df)

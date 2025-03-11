import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV
data = pd.read_csv('temperature_data.csv', parse_dates=['date'])
data.set_index('date', inplace=True)

# Plot temperature data
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['temperature'], marker='o', linestyle='-', color='b', label="Temperature (°C)")

# Find max and min temperatures for annotations
max_temp = data['temperature'].max()
min_temp = data['temperature'].min()
max_date = data['temperature'].idxmax().strftime('%Y-%m-%d')
min_date = data['temperature'].idxmin().strftime('%Y-%m-%d')

# Add annotations
plt.annotate(f'{max_temp}°C on {max_date}', 
             xy=(max_date, max_temp), 
             xytext=(max_date, max_temp + 2),
             arrowprops=dict(facecolor='green', arrowstyle='->'),
             ha='center')

plt.annotate(f'{min_temp}°C on {min_date}', 
             xy=(min_date, min_temp), 
             xytext=(min_date, min_temp - 2),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             ha='center')

# Formatting the plot
plt.title('Daily Temperature Variations')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
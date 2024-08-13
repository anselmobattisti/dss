import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Load the CSV file
file_path = './result.csv'  # Update this path to your file location
data = pd.read_csv(file_path)

# Convert time strings to seconds
data['time_seconds'] = data['time'].apply(lambda x: dt.datetime.strptime(x, '%H:%M:%S.%f').time())
data['time_seconds'] = data['time_seconds'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second + x.microsecond / 1e6)

# Group data by size and calculate the average time and standard error for each size
avg_time_by_size = data.groupby('size')['time_seconds'].agg(['mean', 'sem']).reset_index()

# Create a bar plot with error bars
plt.figure(figsize=(10, 6))
plt.bar(avg_time_by_size['size'], avg_time_by_size['mean'], yerr=avg_time_by_size['sem'], capsize=5, color='skyblue')
plt.title('Segmentation Time by SFC Size')
plt.xlabel('VNF Num')
plt.ylabel('Average Time For Segmenting 10k SFCs (seconds)')
plt.xticks(avg_time_by_size['size'])
plt.grid(axis='y')
plt.savefig('exp1.pdf')
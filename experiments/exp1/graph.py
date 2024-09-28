import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import norm

# Load the CSV file
file_path = './result.csv'  # Update this path to your file location
data = pd.read_csv(file_path)

# data = data[data['size'] != 20]
# data = data[data['size'] != 15]

# Convert time strings to seconds
data['time_seconds'] = data['time'].apply(lambda x: dt.datetime.strptime(x, '%H:%M:%S.%f').time())
data['time_seconds'] = data['time_seconds'].apply(lambda x: x.hour * 3600 + x.minute * 60 + x.second + x.microsecond / 1e6)

# Group data by size and calculate the average time and standard error for each size
avg_time_by_size = data.groupby('size')['time_seconds'].agg(['mean', 'sem']).reset_index()

# Convert size column to string for x-axis labels
avg_time_by_size['size'] = avg_time_by_size['size'].astype(str)

avg_time_by_size['sem'] = avg_time_by_size['sem'] * 95

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

# Create a bar plot with error bars
plt.figure(figsize=(10, 6))

plt.bar(avg_time_by_size['size'], avg_time_by_size['mean'], yerr=avg_time_by_size['sem'], capsize=5, zorder=3, color=(89/255, 117/255, 164/255))

plt.xlabel('Number of VNFs', fontsize=14)
plt.ylabel('Segmentation Time (ms)', fontsize=14)
plt.grid(axis='y', zorder=0, linestyle='--', color="#9E9E9E")
# plt.xticks(rotation=45)  # Rotate the x-axis labels if necessary

# Change the color of the frame border
ax = plt.gca()  # Get the current axes
ax.spines['top'].set_color('none')  # Hide the top spine
ax.spines['right'].set_color('none')  # Hide the right spine
ax.spines['left'].set_color('#9E9E9E')  # Set the left spine color to dark red
ax.spines['bottom'].set_color('#9E9E9E')  # Set the bottom spine color to dark red

plt.ylim([0.000001, 10])  # Start the y-axis at 1 to avoid issues with the log scale

plt.tick_params(axis='x', labelsize=14)  # Increase font size of x-axis values
plt.tick_params(axis='y', labelsize=14)  # Increase font size of y-axis values


# Setting the y-axis to a logarithmic scale
plt.yscale('log')




# Remove the x-axis limit as it may not be needed with string labels
# plt.xlim([avg_time_by_size['size'].min() - 1, avg_time_by_size['size'].max() + 1])

plt.savefig('exp1.pdf')
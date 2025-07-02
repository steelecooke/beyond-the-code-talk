import pandas as pd
import matplotlib.pyplot as plt

# Create a simple dataset (or read from CSV if desired)
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Samples Processed': [23, 45, 12, 67, 34]
}

df = pd.DataFrame(data)

# Calculate average
average = df['Samples Processed'].mean()
print(f"Average samples processed: {average:.2f}")

# Create a basic bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['Day'], df['Samples Processed'], color='skyblue')
plt.axhline(average, color='red', linestyle='--', label=f'Average: {average:.2f}')
plt.title('Samples Processed per Day')
plt.xlabel('Day')
plt.ylabel('Samples Processed')
plt.legend()
plt.tight_layout()

# Save the plot to a file
plt.savefig('/output/plot.png')
print("Plot saved as plot.png")


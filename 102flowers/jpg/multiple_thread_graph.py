from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_excel('output.xlsx') # can also index sheet by name or fetch all sheets
x = df['Multi-Thread'].tolist()
y = df[0].tolist()


# Function to plot 
plt.plot(x,y) 

plt.xlabel('Image Count')
plt.ylabel('Time (seconds)')

plt.title('Multi Thread Execution')
# function to show the plot 
plt.show() 

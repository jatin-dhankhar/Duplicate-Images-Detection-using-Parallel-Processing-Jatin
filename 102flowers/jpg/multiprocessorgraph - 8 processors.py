from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_excel('output.xlsx') # can also index sheet by name or fetch all sheets
x = df['Multi-processor'].tolist()
y = df[0].tolist()

plt.plot(x,y) 

plt.xlabel('Image Count')
plt.ylabel('Time Sorted')

plt.title('Multiple Processor Execution 8 processors')
# function to show the plot 
plt.show() 



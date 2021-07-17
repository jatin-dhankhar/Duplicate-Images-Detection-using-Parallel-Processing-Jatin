from matplotlib import pyplot as plt

import pandas as pd

df = pd.read_excel('output.xlsx') # can also index sheet by name or fetch all sheets
x = df['Multi-Thread'].tolist()
y = df[0].tolist()


x_s_s = df[0].tolist()
y_s_s = df['Single'].tolist()
plt.plot(x_s_s, y_s_s, label='PROCESSOR: 1 THREADS: 0 (Except Main) ( Single processor system)') 


# Multi Processing
x_m_s = df[0].tolist()
y_m_s = df['Multi-processor'].tolist()
plt.plot(x_m_s, y_m_s, label='PROCESSORs: 8 THREADS: 0 (Except Main) ( Multiple Processor system)')


# Multi Threading
x_s_m = df[0].tolist()
y_s_m = df['Multi-Thread'].tolist()
plt.plot(x_s_m, y_s_m, label='PROCESSOR: 1 THREADS: 100 (Except Main) (Multicore using threads)')



plt.xlabel('Image Count')
plt.ylabel('Time (seconds)')

plt.title('Analysing All 3 Executions Together')

plt.legend(loc='best')
plt.show() 

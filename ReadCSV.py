
#read data from csv
import pandas as pd

data = pd.read_csv(r'C:\Users\Tech Vision\Desktop\SQL Sessions\employee.csv')
print(data)

print(data[['name','gender']])
data=data.groupby('gender').size()
print(data)

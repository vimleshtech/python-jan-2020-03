
import pandas as pd

#create empty dataframe
data = pd.DataFrame()
print(data)


#create dataframe from dict and list
d = {'eid':[111,22,4,56],
     'name':['nitin','jatin','divya','ayush'],
     'gender':['male','male','female','male'],
     'salary':[111,333,444,5566]
     }


data = pd.DataFrame(data=d)
print(data)

#print columns
print(data.columns)

#print index or row num
print(data.index)


#print given col
print(data['name'])

print(data[['name','salary']])

#print from top
print(data.head(n=3))

#print from buttom
print(data.tail(n=2))



#info
print(data.info())


#describe #show stat for all numeric col
print(data.describe())


print(data.head(n=3))










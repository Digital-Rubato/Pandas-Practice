import pandas as pd

'''
a = [0,1,2,6]

myvar = pd.Series(a, index = ['w','x','y','z'])

calories = {'day1': 420, 'day2': 380, 'day3': 390}

calvar = pd.Series(calories, index = ['day1', 'day2'])

print(myvar)

print(calvar)

#dict for information
data = {
	'calories': [420, 380, 390],
	'duration': [50, 40, 45],
	'wrench': ['spanner', 'cresent', 'monkey']
}

#dataframe is a 2d data structure
myvar = pd.DataFrame(data)

print(myvar)

#locate df row
print(myvar.loc[[0,1]])

df = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])
print(df)

print(df.loc['day2'])

csv = pd.read_csv('data.csv')

print(csv)
print(csv.to_string)

print(pd.options.display.max_rows)


# change display of maximum rows
#pd.options.display.max_rows = 9999

pd.options.display.max_rows = 60

cf = pd.read_csv('data.csv')

print(cf)


jf = pd.read_json('data.json')

#.to_string() to print entire data frame
#print(jf.to_string())

print(jf)

hf = pd.read_csv('data.csv')
# regular .head() will print 5 rows
print(hf.head(10))
# the same can be said of .tail()
print(hf.tail(10))

rf = pd.read_csv('data.csv')
# summarized information of the data set is output with .info()
print(rf.info())

drf = pd.read_csv('data.csv')

# remove empty cells
new_df = drf.dropna()

print(new_df.to_string())
#added .info() to check how many rows were deleted
print(new_df.info())

inf = pd.read_csv('data.csv')

#removes rows with NULL values
inf.dropna(inplace = True)

print(inf.to_string())
print(inf.info())

fn = pd.read_csv('data.csv')

# .fillna() replaced NULL values with int 130
fn.fillna(130, inplace = True)

print(fn.info())


sf = pd.read_csv('data.csv')

sf['Calories'].fillna(130, inplace = True)

print(sf.info())

mf = pd.read_csv('data.csv')

#calculate the mean
x = mf['Calories'].mean()

#replace empty values
mf['Calories'].fillna(x, inplace = True)
git
print(mf)

mof = pd.read_csv('data.csv')

#calculate mode
x = mof['Calories'].mode()[0]

mof['Calories'].fillna(x, inplace = True)

print(x)

# convert to Date
daf = pd.read_csv('data.csv')

daf['Date'] = pd.to_datetime(daf['Date'])

print(daf.to_string())

#remove rows with a NULL Value in the 'Date' column
daf.dropna(subset=['Date'], inplace = True)
'''





